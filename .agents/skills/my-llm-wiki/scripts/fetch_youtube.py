# /// script
# requires-python = ">=3.12"
# dependencies = ["yt-dlp>=2025.1.1"]
# ///
"""Fetch a YouTube transcript into a wiki's raw/ layer as timestamped markdown.

Three jobs, in order: parse the video id from the URL, ask yt-dlp for the metadata
and the caption tracks (no media is downloaded), and turn the best caption track
into sections headed by their start time. Auto-captions have no punctuation and no
headings; the `## 12:30` headings are what a source page cites,
as `[[raw/youtube-<id>#12:30|cite]]`.

Identity is the raw path `raw/youtube-<id>.md`, with the video id kept verbatim —
NOT the title, which changes (CONVENTIONS.md § Identity and dedup). Ids are
`[A-Za-z0-9_-]{11}`, already filename-safe.

Track choice: manual subtitles in `--lang` first, then the auto-captions in
`--lang`, then the auto-captions in the video's own language. A translated
auto-caption track is never used when an original one exists.

Usage:
  uv run --script fetch_youtube.py --url https://www.youtube.com/watch?v=<id> --wiki-dir wiki-<slug>

Receipt (stdout):
  {"origin": "youtube", "original_path": <url>, "title", "source_url",
   "authors": [...], "published_date", "raw_path", "video_id", "channel",
   "duration", "transcript", "chars", ["warning"]}
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

VIDEO_ID = re.compile(r"^[A-Za-z0-9_-]{11}$")

# Path prefixes that carry the id as the next segment: /shorts/<id>, /live/<id>, ...
ID_PATH_PREFIXES = {"shorts", "live", "embed", "v", "e"}


def video_id(url: str) -> str:
    parsed = urlparse(url if "://" in url else f"https://{url}")
    host = (parsed.hostname or "").lower().removeprefix("www.").removeprefix("m.")
    parts = [p for p in parsed.path.split("/") if p]
    candidate = None
    if host == "youtu.be" and parts:
        candidate = parts[0]
    elif host.endswith("youtube.com") or host == "youtube-nocookie.com":
        if parts[:1] == ["watch"]:
            candidate = (parse_qs(parsed.query).get("v") or [None])[0]
        elif len(parts) >= 2 and parts[0] in ID_PATH_PREFIXES:
            candidate = parts[1]
    if not candidate or not VIDEO_ID.match(candidate):
        raise SystemExit(f"no YouTube video id in {url}")
    return candidate


def timestamp(seconds: float) -> str:
    s = int(seconds)
    h, m, s = s // 3600, s % 3600 // 60, s % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def pick_track(info: dict, lang: str) -> tuple[str, str, str] | None:
    """(kind, language, json3 url) for the best caption track, or None."""

    def json3(tracks: list[dict]) -> str | None:
        return next((t["url"] for t in tracks if t.get("ext") == "json3"), None)

    def find(table: dict, *langs: str) -> tuple[str, str] | None:
        for want in langs:
            for key, tracks in table.items():
                if key == want or key.split("-")[0] == want:
                    url = json3(tracks)
                    if url:
                        return key, url
        return None

    manual = info.get("subtitles") or {}
    auto = info.get("automatic_captions") or {}
    native = info.get("language")
    for kind, table, langs in (
        ("manual", manual, [lang]),
        ("auto", auto, [f"{lang}-orig"]),
        ("manual", manual, [native] if native else []),
        ("auto", auto, [f"{native}-orig", native] if native else []),
    ):
        # Auto-caption tables list every translation too; only "<lang>-orig" or
        # the native language is the real recognizer output.
        hit = find(table, *langs) if langs else None
        if hit:
            return kind, hit[0].removesuffix("-orig"), hit[1]
    return None


def cues(ydl: YoutubeDL, url: str) -> list[tuple[float, str]]:
    """(start seconds, text) per caption event, with rolling-caption repeats dropped."""
    data = json.loads(ydl.urlopen(url).read().decode("utf-8"))
    out: list[tuple[float, str]] = []
    for event in data.get("events", []):
        text = "".join(seg.get("utf8", "") for seg in event.get("segs") or [])
        text = " ".join(text.split())
        if text:
            out.append((event.get("tStartMs", 0) / 1000, text))
    return out


def sections(
    lines: list[tuple[float, str]], chapters: list[dict], every: int
) -> list[tuple[float, str | None, str]]:
    """Group cues into (start, chapter title, text). A section breaks at every
    chapter start and otherwise after `every` seconds, at the next cue."""
    starts = sorted((c["start_time"], c.get("title")) for c in chapters if c.get("start_time") is not None)
    out: list[tuple[float, str | None, list[str]]] = []
    next_chapter = 0
    for start, text in lines:
        chapter = None
        while next_chapter < len(starts) and starts[next_chapter][0] <= start:
            chapter = starts[next_chapter][1]
            next_chapter += 1
        if not out or chapter or start - out[-1][0] >= every:
            out.append((start, chapter, []))
        out[-1][2].append(text)
    return [(start, chapter, " ".join(texts)) for start, chapter, texts in out]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--url", required=True, help="YouTube video URL.")
    parser.add_argument("--wiki-dir", required=True, help="Path to wiki-<slug>/.")
    parser.add_argument("--lang", default="en", help="Preferred transcript language (default: en).")
    parser.add_argument("--section-seconds", type=int, default=60, help="Target section length (default: 60).")
    parser.add_argument("--output", default=None, help="Override the raw path (default: raw/youtube-<id>.md).")
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
        stream.reconfigure(encoding="utf-8")

    wiki_dir = Path(args.wiki_dir).expanduser().resolve()
    if not (wiki_dir / "wiki").is_dir():
        raise SystemExit(f"not a wiki dir (no wiki/ inside): {wiki_dir}")

    vid = video_id(args.url)
    source_url = f"https://www.youtube.com/watch?v={vid}"

    with YoutubeDL({"quiet": True, "no_warnings": True, "skip_download": True, "noplaylist": True}) as ydl:
        try:
            info = ydl.extract_info(source_url, download=False)
        except DownloadError as err:
            raise SystemExit(f"fetch failed for {args.url}: {err}") from None
        track = pick_track(info, args.lang)
        if not track:
            raise SystemExit(f"no transcript available for {args.url} (no captions in {args.lang} or the video's language)")
        kind, lang, track_url = track
        body_sections = sections(cues(ydl, track_url), info.get("chapters") or [], args.section_seconds)

    title = info.get("title") or vid
    channel = info.get("channel") or info.get("uploader")
    upload = info.get("upload_date")  # YYYYMMDD
    published = f"{upload[:4]}-{upload[4:6]}-{upload[6:]}" if upload else None
    duration = timestamp(info["duration"]) if info.get("duration") else None

    raw_path = Path(args.output) if args.output else wiki_dir / "raw" / f"youtube-{vid}.md"
    raw_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "---",
        f"title: {json.dumps(title)}",
        f"authors: {json.dumps([channel] if channel else [])}",
        f"published_date: {json.dumps(published) if published else 'null'}",
        f"source_url: {source_url}",
        "origin: youtube",
        f"fetched: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"video_id: {json.dumps(vid)}",
        f"channel: {json.dumps(channel) if channel else 'null'}",
        f"duration: {json.dumps(duration) if duration else 'null'}",
        f"transcript: {kind}-{lang}",
        "---",
        "",
        f"# {title}",
        "",
    ]
    if kind == "auto":
        lines += ["*Auto-generated captions: no punctuation, names may be misheard.*", ""]
    for start, chapter, text in body_sections:
        lines += [f"## {timestamp(start)}", ""]
        if chapter:
            lines += [f"**{chapter}**", ""]
        lines += [text, ""]
    raw_path.write_text("\n".join(lines), encoding="utf-8")

    chars = sum(len(text) for _, _, text in body_sections)
    receipt = {
        "origin": "youtube",
        "original_path": args.url,
        "title": title,
        "source_url": source_url,
        "authors": [channel] if channel else [],
        "published_date": published,
        "raw_path": raw_path.relative_to(wiki_dir).as_posix(),
        "video_id": vid,
        "channel": channel,
        "duration": duration,
        "transcript": f"{kind}-{lang}",
        "chars": chars,
    }
    if chars < 500:
        receipt["warning"] = "transcript under 500 chars — a music video, a short, or a broken caption track"
        print(f"WARN: {receipt['warning']} ({args.url})", file=sys.stderr)
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

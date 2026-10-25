# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Shallow-clone a git repo into a wiki's raw/ layer and report its HEAD SHA.

The clone is the **raw artifact** for a repo source, exactly as a copied note is
the raw artifact for a local one. It lands at

    <wiki-dir>/raw/repos/.github-<owner>-<repo>/

Dot-prefixed on purpose: Obsidian ignores dot-directories, so a 40 MB checkout
never shows up in the vault, the graph, or search. It is a **regenerable cache** —
deleting it is always safe, and re-ingesting the repo refreshes it in place rather
than skipping it (CONVENTIONS.md § Immutability).

The same clone may be refreshed from Windows and from WSL. Each clone pins
`core.autocrlf=false` (identical LF bytes on both sides, so neither sees the
other's checkout as modified) and `core.longpaths=true` (deep repos under a deep
wiki path pass Windows' 260-char limit). A failed refresh never loses the cache:
a re-clone goes to a sibling temp dir and replaces the old clone only on success.

The receipt carries the shared adapter core (SOURCES.md § The adapter contract).
A repo has no byline or publish date, so `authors` is the owner and
`published_date` is the date of the HEAD commit — the date of the snapshot.

Usage:
  uv run --script clone_repo.py --url https://github.com/<owner>/<repo> --wiki-dir wiki-<slug>
  uv run --script clone_repo.py --url <url> --wiki-dir <dir> --branch develop

Receipt (stdout):
  {"origin": "repo", "original_path": <url>, "title": "<owner>/<repo>", "source_url",
   "authors": [<owner>], "published_date", "raw_path": "raw/repos/.github-<owner>-<repo>/",
   "owner", "repo", "branch", "clone_path", "commit_sha", "action": "cloned"|"updated"}
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path

REPO_URL_RE = re.compile(
    r"(?:https?://|git@)(?:www\.)?github\.com[/:]"
    r"(?P<owner>[^/\s]+)/(?P<repo>[^/\s#?]+?)(?:\.git)?"
    r"(?:/(?:tree|blob)/(?P<branch>[^/\s?#]+))?/?$",
    re.IGNORECASE,
)

# Pinned in every clone's .git/config, so Windows and WSL git agree on the checkout.
CLONE_CONFIG = {"core.autocrlf": "false", "core.longpaths": "true"}

# Fail instead of waiting on a credential prompt (a typo'd or private repo URL).
GIT_ENV = {**os.environ, "GIT_TERMINAL_PROMPT": "0", "GCM_INTERACTIVE": "never"}


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd, cwd=cwd, env=GIT_ENV, check=True, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )


def parse_repo_url(url: str, branch_override: str | None) -> tuple[str, str, str | None]:
    """(owner, repo, branch) — branch is None when the URL does not pin one."""
    match = REPO_URL_RE.match(url.strip())
    if not match:
        raise SystemExit(f"not a recognizable GitHub repo URL: {url}")
    return match["owner"], match["repo"], branch_override or match["branch"]


def force_rmtree(path: Path) -> None:
    """rmtree that also removes read-only files (git's pack files on Windows)."""

    def clear_readonly(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)

    shutil.rmtree(path, onexc=clear_readonly)


def clone(clone_path: Path, clone_url: str, branch: str | None) -> None:
    """Clone into a sibling temp dir, then swap it in; the old clone survives a failure."""
    tmp_path = clone_path.with_name(clone_path.name + ".tmp")
    if tmp_path.exists():
        force_rmtree(tmp_path)
    tmp_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["git", "clone", "--depth=1"]
    for key, value in CLONE_CONFIG.items():
        cmd += ["--config", f"{key}={value}"]
    if branch:
        cmd += ["--branch", branch]
    try:
        run(cmd + [clone_url, str(tmp_path)])
    except subprocess.CalledProcessError:
        if tmp_path.exists():
            force_rmtree(tmp_path)
        raise
    if clone_path.exists():
        force_rmtree(clone_path)
    tmp_path.rename(clone_path)


def update(clone_path: Path, branch: str) -> None:
    # Clones made before CLONE_CONFIG existed: pin it, and re-checkout once if a
    # line-ending setting changed, since the working tree holds the old endings.
    renormalize = False
    for key, value in CLONE_CONFIG.items():
        current = subprocess.run(
            ["git", "config", "--local", "--get", key], cwd=clone_path, env=GIT_ENV, capture_output=True, text=True
        ).stdout.strip()
        if current != value:
            run(["git", "config", "--local", key, value], cwd=clone_path)
            renormalize |= key == "core.autocrlf"
    # A shallow clone tracks only its own branch, so name the refspec explicitly:
    # that also covers switching to a branch the clone has never seen.
    run(["git", "fetch", "--depth=1", "origin", f"+refs/heads/{branch}:refs/remotes/origin/{branch}"], cwd=clone_path)
    if renormalize:
        run(["git", "rm", "-r", "-q", "--cached", "."], cwd=clone_path)
    run(["git", "checkout", "-f", "-B", branch, f"origin/{branch}"], cwd=clone_path)


def current_branch(clone_path: Path) -> str:
    return run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=clone_path).stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    # --repo is the old spelling, kept so existing calls keep working.
    parser.add_argument("--url", "--repo", dest="url", required=True, help="GitHub repo URL (may include /tree/<branch>).")
    parser.add_argument("--wiki-dir", required=True, help="Path to wiki-<slug>/.")
    parser.add_argument("--branch", default=None, help="Branch override (default: the repo's default branch).")
    parser.add_argument("--output", default=None, help="Override the clone path, inside the wiki dir (default: raw/repos/.github-<owner>-<repo>/).")
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):  # Windows consoles default to cp1252
        stream.reconfigure(encoding="utf-8")

    owner, repo, branch = parse_repo_url(args.url, args.branch)
    wiki_dir = Path(args.wiki_dir).expanduser().resolve()
    if not (wiki_dir / "wiki").is_dir():
        raise SystemExit(f"not a wiki dir (no wiki/ inside): {wiki_dir}")

    default_path = wiki_dir / "raw" / "repos" / f".github-{owner}-{repo}".lower()
    clone_path = Path(args.output).expanduser().resolve() if args.output else default_path
    if not clone_path.is_relative_to(wiki_dir):
        raise SystemExit(f"--output must be inside the wiki dir ({wiki_dir}): {clone_path}")
    clone_url = f"https://github.com/{owner}/{repo}.git"

    try:
        if (clone_path / ".git").is_dir():
            action = "updated"
            try:
                update(clone_path, branch or current_branch(clone_path))
            except subprocess.CalledProcessError as err:
                print(f"warn: update failed ({err.stderr.strip()}), re-cloning", file=sys.stderr)
                clone(clone_path, clone_url, branch)
                action = "cloned"
        else:
            clone(clone_path, clone_url, branch)
            action = "cloned"
        published_date = run(["git", "log", "-1", "--format=%cs"], cwd=clone_path).stdout.strip() or None
        head_branch = current_branch(clone_path)
        commit_sha = run(["git", "rev-parse", "HEAD"], cwd=clone_path).stdout.strip()
    except subprocess.CalledProcessError as err:
        raise SystemExit(f"git failed: {' '.join(err.cmd)}\n{(err.stderr or '').strip()}")
    except FileNotFoundError:
        raise SystemExit("git not found on PATH")

    rel_path = clone_path.relative_to(wiki_dir).as_posix()
    receipt = {
        "origin": "repo",
        "original_path": args.url,
        "title": f"{owner}/{repo}",
        "source_url": f"https://github.com/{owner}/{repo}",
        "authors": [owner],
        "published_date": published_date,
        "raw_path": f"{rel_path}/",
        "owner": owner,
        "repo": repo,
        "branch": head_branch,
        "clone_path": rel_path,
        "commit_sha": commit_sha,
        "action": action,
    }
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

---
title: "Boards and rules"
subtitle: "Define your team's process with custom boards, agent actions, and approval policies."
authors: []
published_date: null
source_url: https://factory.mastra.ai/configure/boards-and-rules.md
origin: llms-txt
llms_txt: https://factory.mastra.ai/llms.txt
section: "Docs / Configuration"
fetched: 2026-10-25T18:10:21Z
---

# Boards and rules

Boards and rules turn your team's process into actions that Factory can run. A board defines the phases of a work item, such as Queued, Checking, and Done. Rules determine what happens at each step. For example, entering Checking can start an agent, while moving to Done can require a person's approval.

Factory includes Work and Review boards. Add a custom board when you need a different process, such as a quality check or release review. For everyday tasks and approvals on the built-in boards, see [Work items](https://factory.mastra.ai/using/work-and-approvals).

## Choose what to customize

| What you want to do                       | Where to configure it                                                 |
| ----------------------------------------- | --------------------------------------------------------------------- |
| Add phases and allowed moves between them | `defineBoard()` and the `MastraFactory` constructor's `boards` array. |
| Start an agent when a card enters a phase | The phase's `onEnter` handler.                                        |
| Run an action when a card leaves a phase  | The phase's `onExit` handler.                                         |
| Require approval before a move            | The board's `transitionPolicy`.                                       |
| React to GitHub or Linear events          | The corresponding integration's event rules.                          |
| React to an agent's tool result           | The board's `tools.<toolName>.onResult` handler.                      |

## Define and install a board

This example adds a Quality board alongside Work and Review. It defines three phases and the allowed moves between them. The next section adds an agent action when a card enters Checking.

Add the board definition to `src/mastra/index.ts` and pass it in the existing `MastraFactory` configuration. Preserve your server's storage, authentication, encryption, sandbox, and integration settings. The configuration below shows a minimal server.

```typescript title="src/mastra/index.ts"
import { Mastra } from '@mastra/core'
import { MastraFactory, defineBoard } from '@mastra/factory'
import { LibSQLFactoryStorage } from '@mastra/libsql'

const qualityBoard = defineBoard({
	id: 'quality',
	title: 'Quality',
	initialPhase: 'queued',
	phases: {
		queued: { title: 'Queued', kind: 'resting', outcomes: { start: 'checking' } },
		checking: {
			title: 'Checking',
			kind: 'working',
			role: 'quality-checker',
			outcomes: { pass: 'done', retry: 'queued' },
		},
		done: { title: 'Done', kind: 'terminal' },
	},
})

const factory = new MastraFactory({
	storage: new LibSQLFactoryStorage({ id: 'factory-storage', url: 'file:./factory.db' }),
	boards: [qualityBoard],
})

export const mastra = new Mastra(await factory.prepare())
await factory.finalize()
```

The phase `kind` distinguishes waiting, agent work, and completion. The working phase also requires a `role`. Here, `outcomes` defines the allowed moves without moving cards automatically. See the [board definition reference](https://factory.mastra.ai/reference/mastra-factory-api) for field details and validation rules.

After restarting the server, open **Quality** in the Factory UI and check that its three phases are listed. Custom boards use the existing board UI. You don't need to build another interface.

## Run actions on phase changes

To start a quality check when a manual card enters Checking, add this `onEnter` handler to the `checking` phase above. For this repository-review prompt, first configure a [model provider](https://factory.mastra.ai/configure/models) and a [repository sandbox](https://factory.mastra.ai/configure/sandboxes).

```typescript
onEnter: {
	manual: context => ({
		type: 'invokeSkill',
		idempotencyKey: `${context.ingress.id}:quality-check`,
		role: 'quality-checker',
		prompt:
			'Review the work item against the repository. Summarize your findings without changing files, then wait for a person to choose pass or retry.',
	})
}
```

After restarting the server, create a manual work item on **Quality** and move it from **Queued** to **Checking** to run the prompt. Review the agent's findings before choosing an outcome.

This handler applies to manual cards. For other sources and available actions, see [rule handlers](https://factory.mastra.ai/reference/mastra-factory-api). To enforce human approval rather than rely on the prompt, add a [transition policy](https://factory.mastra.ai/reference/mastra-factory-api).

## Configure tool rules

Tool rules react to the results of an agent's tool calls. Add this `tools` property alongside `phases` in the same Quality board definition. It sends a warning to the session when `execute_command` reports a tool error during Checking.

```typescript
tools: {
	execute_command: {
		onResult: context => {
			if (context.item.stages[0] !== 'checking' || context.result.status !== 'error') return

			return {
				type: 'notify',
				idempotencyKey: `${context.ingress.id}:quality-command-error`,
				title: 'Quality check command failed',
				body: 'Inspect the tool error before continuing the quality check.',
				level: 'warning',
			}
		}
	}
}
```

The rule leaves the card in its current phase. A command that returns a nonzero exit code isn't necessarily a tool error. To handle that case, inspect the command's returned value as well.

This rule applies only to Quality. It doesn't change the built-in Work board's `submit_plan` handler, which checks for an approved plan before requesting a move to Building. See [tool-result handlers](https://factory.mastra.ai/reference/mastra-factory-api) for the result format and handler behavior.

## Configure rules for integration events

GitHub and Linear event rules are configured on their integrations, not on the board. Use those rules for events such as an issue opening or a pull request merging. Keep default behavior you still need when overriding an event handler. See [GitHub configuration](https://factory.mastra.ai/configure/github) or [Linear configuration](https://factory.mastra.ai/configure/linear) for integration setup.

## Related

- [MastraFactory API](https://factory.mastra.ai/reference/mastra-factory-api)
- [GitHub configuration](https://factory.mastra.ai/configure/github)
- [Linear configuration](https://factory.mastra.ai/configure/linear)

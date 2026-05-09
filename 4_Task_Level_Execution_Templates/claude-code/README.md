# Claude Code Harness (under L4)

This subtree describes **how Claude Code operates** the AI-NPI Factory: agents, commands, skills, hooks, worktrees, MCP connectors, and context policy. It lives inside Layer 4 because it governs **task-level execution**, not Factory-wide principles.

## Mental Model
- **Main Agent** = factory foreman / orchestrator. Holds the plan, delegates, integrates.
- **Subagents** = context-isolated specialists. Used to keep main context clean.
- **Skills** = repeatable, reusable expert work packages.
- **Commands** = standard execution buttons mapped to L2 modules and L4 templates.
- **Hooks** = automatic checks, blockers, and alerts.
- **Worktree** = parallel production line (one branch, one purpose).
- **MCP** = ports to external systems.
- **Context Policy** = memory & context-window discipline.

## Structure
```
claude-code/
├─ README.md                        ← this file
├─ agents/
│   ├─ README.md
│   ├─ agent-candidates.md
│   └─ context-isolation-policy.md
├─ commands/                        ← 7 standard commands
├─ skills/                          ← candidates only in v0.1.0
├─ hooks/                           ← candidates only in v0.1.0
├─ worktree/
└─ mcp/
```

## v0.1.0 Status
- **Documented**: agents (principles + candidates), commands (7 files), worktree policy.
- **Candidate-only (no implementation)**: skills, hooks, MCP connectors.
- **Out of scope (v0.1.0)**: actual hook scripts, skill packages, MCP server code, automation CLI.

## How This Connects to L1–L4
- L1 (Decision Principles) defines when a Human Control Point fires; harness wires this via the `on-critical-decision` hook and the `ask-chatgpt-decision` command.
- L2 modules map to commands one-to-one or many-to-one (e.g., `validate-output` ↔ `06_verification`).
- L3 Playbooks declare which agents / commands / skills they activate.
- L4 templates are the inputs/outputs of every command run.

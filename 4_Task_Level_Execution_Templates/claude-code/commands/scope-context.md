# Command: scope-context

## Purpose
Decide what to read **and what NOT to read** before any work starts. Keep main context lean.

## When to Run
- At the start of any non-trivial task.
- Whenever the main agent is tempted to "just read everything to be safe".

## Inputs
- Current `NPI_Brief.md` (or its draft).
- Affected Objects from the Playbook ontology.
- Question(s) to answer.

## Procedure
1. State the question(s) in one line each.
2. List candidate files / paths.
3. Mark each candidate as **READ** or **DO NOT READ** with a one-line reason.
4. If candidates exceed the budget, delegate broad sweeps to `context-scout` subagent instead of reading directly.
5. Record the resulting allowlist into the BuildLog or Worklist task entry.

## Output
```
## Context Scope — <task>
Questions:
- ...

READ:
- path/to/file.md — reason
- src/foo.ts — reason

DO NOT READ:
- 3_Domain_Project_Playbooks/<other>/  — out of scope for this task
- L1 docs — already internalized
- generated/* — noise

Delegated:
- context-scout: "Where is X defined?" (paths: src/**)
```

## Acceptance Criteria
- Both READ and DO-NOT-READ lists are present.
- Each entry has a reason.
- Total READ budget fits the current step.

## Anti-patterns
- "Read everything" lists.
- DO-NOT-READ omitted (silent over-reading).
- Pulling subagent transcripts back into main context.

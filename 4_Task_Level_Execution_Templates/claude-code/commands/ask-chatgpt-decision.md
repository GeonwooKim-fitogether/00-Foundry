# Command: ask-chatgpt-decision

## Purpose
Package a strategic question that Claude Code is unable or unwilling to settle alone, and route it to ChatGPT (or another decision partner) for judgment.

## When to Run
- A Critical Decision is open and needs an outside perspective.
- The decision is high-stakes, low-reversibility, or cross-cutting in a way Claude Code's scope can't see.
- Two or more options remain after `review-risk` and the recommendation is not obvious.

## Procedure
1. Run `review-risk` first; this command is only for cases that already cleared that bar.
2. Fill the Decision Package below in full. Empty fields disqualify the request.
3. Send the package as a single message to ChatGPT (no extra files unless explicitly requested).
4. Record the request and the answer in `NPI_BuildLog.md` Critical Decisions Log.

## Decision Package (mandatory format)

```
Context Summary:
Project:
Current Task:
Decision Needed:
Options:
  - A) ...
  - B) ...
  - C) ...
Claude Code Recommendation:
Evidence:
Risks:
Reversibility:
Impact on User Goals:
Requested Decision:
```

### Field Notes
- **Context Summary**: 3–5 sentences. Enough for an outsider to grasp the situation cold.
- **Project**: Playbook ID + version.
- **Current Task**: Brief title + which AC items are at stake.
- **Decision Needed**: a single sentence question.
- **Options**: each option self-contained.
- **Claude Code Recommendation**: pick one option; do not punt.
- **Evidence**: bullet points, each with source.
- **Risks**: top 1–3 risks per option.
- **Reversibility**: reversible / partially reversible / irreversible.
- **Impact on User Goals**: tie back to the project's goal stated in `NPI_Brief.md`.
- **Requested Decision**: what exact answer would unblock execution.

## Acceptance Criteria
- All fields filled.
- Recommendation is concrete (not "depends").
- Reversibility is stated.
- Outcome recorded back in BuildLog within the same session.

## Anti-patterns
- Sending a wall of context with no recommendation.
- Asking ChatGPT to "think about it" instead of answering a specific question.
- Skipping the BuildLog record of the answer.

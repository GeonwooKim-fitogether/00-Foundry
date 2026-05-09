# Command: review-risk

## Purpose
Decide whether the current situation is a **Critical Decision** that must escalate to a Human Control Point, and if so, prepare the decision package.

## When to Run
- Whenever the executor smells one of the four Critical Decision triggers.
- Periodically during long tasks (mid-task risk sweeps).
- Before any irreversible action.

## Critical Decision Triggers (from L1/01)
1. Irreversible change.
2. Meaningful scope / budget / schedule change.
3. Risk-level upgrade.
4. Acceptance Criteria change.

## Procedure
1. State the situation in 2–3 sentences.
2. Test against the four triggers. If none → continue under Automated Control.
3. If any trigger fires → freeze execution, run `risk-reviewer` subagent if cross-file scan is needed.
4. Build the decision package (see `ask-chatgpt-decision.md` for ChatGPT escalation, or send to the human owner directly).
5. Record the trigger and outcome in `NPI_BuildLog.md` Critical Decisions Log.

## Output
- Yes/no escalation decision.
- If yes: a decision package (for ChatGPT or human).
- BuildLog entry.

## Acceptance Criteria
- Trigger evaluated against all 4 conditions, not just one.
- Decision package (when needed) is complete.
- BuildLog reflects the outcome.

## Anti-patterns
- Treating every uncertainty as Critical (paralysis).
- Treating no uncertainty as Critical (recklessness).
- Asking the human without evidence + recommendation attached.

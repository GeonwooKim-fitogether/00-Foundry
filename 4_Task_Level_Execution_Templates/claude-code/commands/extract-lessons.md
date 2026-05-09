# Command: extract-lessons

## Purpose
Convert lived experience into **specific edits to L1/L2/L3** (or marked "no Factory change needed" with reason).

## When to Run
- After a task or project closes (Final Control Point passed or task discarded).
- After a hotfix is verified.

## Inputs
- `NPI_BuildLog.md`, `NPI_Verification.md`, Risk register, Metrics report (if any).

## Procedure
1. Run `lesson-extractor` subagent on the inputs (or do it directly if small).
2. Produce a keep / change / drop list. Each item must point to a concrete edit target (file + section), or be marked "no Factory change needed" with reason.
3. File proposals into the relevant Factory layer. Bump the Factory version per Semver if structural.
4. If the lesson is project-specific (not Factory-wide), file it inside the Playbook instead of L1/L2.

## Output
- Retro note with keep / change / drop.
- Concrete edits or PRs.

## Acceptance Criteria
- Each item points to a file/section.
- Each item is owned by someone.
- At least one item is acted on or explicitly closed as "no change".

## Anti-patterns
- "We learned a lot" without edits.
- Vague items like "communicate better".
- Lessons that disappear into a parking lot.

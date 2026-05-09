# Worktree Policy

## Principles
1. **Parallel work goes to worktrees.** Independent experiments or independent features each get their own worktree.
2. **`main` is the integration baseline.** It never holds in-flight work.
3. **One worktree, one purpose.** A worktree has exactly one declared deliverable or experiment.
4. **A worktree carries its own AC.** The deliverable and AC are stated in a Brief (or Brief excerpt) inside the worktree.
5. **Final Control Point decides the fate.** At the end, the worktree is **merged**, **archived**, or **discarded** — never left to drift.

## When to Create
- Independent experiments that should not contaminate `main`.
- Features that may be discarded.
- Risky refactors where rollback must be cheap.
- Two changes that touch overlapping files but must be evaluated independently.

## When NOT to Create
- A 5-line fix that belongs on the current branch.
- Work that has no chance of being discarded.
- Just to "feel safe" — the cost is real (context switch, sync overhead).

## Naming
- Branch / worktree directory: `wt/<purpose-kebab>` (e.g., `wt/verification-runner-skill`).
- One Brief per worktree, named `NPI_Brief.md` at the worktree root or under the project's working area.

## Lifecycle
1. **Create**: branch from `main`, declare purpose + AC.
2. **Work**: under Automated Control; Critical Decisions still escalate.
3. **Final Control Point**: AC verified.
4. **Decide**:
   - **Merge** to `main` if AC met and integration safe.
   - **Archive** (keep history, don't merge) if the work is reference-only.
   - **Discard** (delete branch) if the experiment failed — record lessons before deletion.
5. **Record**: the decision and reason go into the parent project's BuildLog.

## Anti-patterns
- Long-lived worktrees with no closure.
- Multiple worktrees doing the same work without a merge plan.
- Discarding without recording lessons.
- Merging without Final Control Point.

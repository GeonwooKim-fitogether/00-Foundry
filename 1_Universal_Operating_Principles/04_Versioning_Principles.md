# 04 — Versioning Principles

## Semver for the Factory
The Factory itself uses [Semver](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **MAJOR** — incompatible change to the 4-Layer Frame, layer contracts, or required template sections.
- **MINOR** — backwards-compatible additions (new module, new template, new optional section).
- **PATCH** — clarifications, typo fixes, non-structural edits.

Initial Factory version: **0.1.0**.

## Semver for Projects
Projects on the Factory should also use Semver where applicable. v0.x indicates pre-stable.

## Where the Version Lives
- `factory.yaml → factory.version` is the source of truth for Factory version.
- Each Playbook (e.g., `ai-npi-platform/`) declares its own version inside its `00_Project_Brief.md` or `NPI_Brief.md`.

## Change Log Discipline
- Every released change updates `CHANGELOG.md`.
- Every entry references which layer(s) changed and whether the change is MAJOR / MINOR / PATCH.

## Compatibility Promise (v0.x)
While the Factory is on `0.x`, MINOR bumps may include adjustments that would normally be MAJOR. Stability is promised from `1.0.0` onward.

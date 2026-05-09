# NPI_Patchnote — <patch name>

> Template (v0.1.0). Lightweight record for a hotfix or patch. Apply ACDE: do not patch without an AC for the patch itself.

## Identity
- **Patch ID**: P-<NNN>
- **Date**: <YYYY-MM-DD>
- **Severity**: low | medium | high | critical
- **Source signal**: <bug report / metric breach / risk trigger>

## Symptom (observed)
What is happening, where, and how it was detected.

## Root Cause (suspected → confirmed)
- Suspected: …
- Confirmed by: <evidence>

## Affected Objects
```
- ObjectA
```

## Acceptance Criteria for this Patch
- AC-P1: Given …, When …, Then …
- AC-P2: <regression check that the original symptom no longer occurs>

## Change
- Files / areas changed:
- Reversibility: reversible | irreversible (if irreversible → Human Control Point)

## Verification
| AC ID | Method | Result | Evidence |
|---|---|---|---|
| AC-P1 | | Pass / Fail | |

## Follow-ups
- Add to risk register? Y/N
- Retro item? Y/N

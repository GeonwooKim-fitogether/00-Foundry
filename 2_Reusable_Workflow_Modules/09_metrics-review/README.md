# Module: metrics-review

> Placeholder (v0.1.0).

## Purpose
Compare reality against the Object Metrics declared in the project ontology and AC.

## Inputs
- Project `domain-ontology.md` (Object Metrics section).
- Telemetry / observed values / qualitative reports.

## Outputs
- Metrics report (target vs. observed, deltas, anomalies).
- Issues / hotfix triggers if metrics breach thresholds.

## Acceptance Criteria
- Every Object Metric declared in the ontology has a current value or an explicit "not yet measured".
- Threshold breaches generate concrete follow-ups (Worklist items or Patchnotes).

## Control Points
Start (metric scope agreed) → Automated (data pulls / dashboard refresh) → Human if Critical → Final (report accepted).

## Checklist
- [ ] All declared metrics covered
- [ ] Anomalies attached to follow-ups
- [ ] Trend (vs. last review) recorded if available

## Anti-patterns
- Reviewing only metrics that look good.
- Reporting without follow-up actions on breaches.

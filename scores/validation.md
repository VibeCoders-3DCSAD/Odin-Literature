# Validation of Automated Scores vs Existing Annotations

**Caveat:** the annotations (`odin_topics` / `topic_relevance` in the `_summarized.json`
files) were AI-generated under the **old** topic taxonomy (1.A-14.C) before the thesis
overhaul. They are a sanity check only — not ground truth. Use them to confirm the
automated scorer points in the same direction, then re-calibrate thresholds with judgment.

- Papers with at least one `medium`/`high` annotated topic: **382** / 518
- Point-biserial correlation (annotated med/high vs best combined score): **0.126**
- Point-biserial correlation (annotated high vs best combined score): **0.178**

Confusion vs `supporting_min=0.3` threshold (positive = automated relevance >= threshold):

| | annotated relevant | annotated not |
|---|---|---|
| automated >= thr | 349 (TP) | 114 (FP) |
| automated < thr  | 33 (FN) | 22 (TN) |

- Sensitivity (recall of annotated-relevant): **0.914**
- Specificity: **0.162**
- Precision: **0.754**
- F1: **0.826**

> If sensitivity is very low, many annotated-relevant papers fall below the threshold:
> lower `tiers.supporting_min` in config/modules.yaml. If specificity is very low,
> the threshold is too permissive. Adjust in config and re-run `scripts/score.py` only.
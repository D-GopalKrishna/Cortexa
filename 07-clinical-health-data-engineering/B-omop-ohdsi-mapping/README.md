# OMOP/OHDSI CDM Mapping

Map a real (or synthetic) clinical dataset into the **OMOP Common Data
Model** — the standard OHDSI uses to make observational health data queryable
the same way across institutions. This is the piece of the requirement list
about large-scale, cross-institution observational health data, distinct
from [A](../A-healthcare-data-standards-interop/)'s single-recording
standards work.

## Dataset

- [Synthea](https://synthetichealth.github.io/synthea/) — generates fully
  synthetic but realistic patient records (already available in OMOP CDM
  format as an export option) — start here, zero data-access friction
- [MIMIC-IV](https://physionet.org/content/mimiciv/) (via PhysioNet, requires
  credentialed access + a short training course) — real de-identified ICU
  data, has an official OMOP CDM conversion ETL published by MIT-LCP if you
  want the real-data version once Synthea feels too easy

## Suggested stack

- [OHDSI's `CommonDataModel`](https://github.com/OHDSI/CommonDataModel) DDL
  scripts to stand up an empty OMOP CDM schema (PostgreSQL or SQLite for a
  local v1)
- [Athena](https://athena.ohdsi.org/) — OHDSI's vocabulary browser, needed to
  map source codes (e.g. ICD, LOINC) to OMOP `concept_id`s
- Python (`pandas`/SQL) for the actual ETL from source format into CDM tables

## Milestones

1. Stand up an empty local OMOP CDM schema; understand its core tables
   (`person`, `visit_occurrence`, `condition_occurrence`, `measurement`,
   `concept`)
2. Load Synthea's synthetic patients directly (Synthea can export pre-mapped
   OMOP CDM) — verify you can run a basic OHDSI-style cohort query (e.g.
   "patients with condition X") against it
3. Harder version: take Synthea's *raw* (non-OMOP) export and do the ETL
   yourself — map source concepts to standard OMOP `concept_id`s via Athena,
   populate `measurement`/`condition_occurrence` from scratch
4. Tie back to this repo's physiological data: model a sleep-stage study
   (from 01-A) as `measurement` rows in the same CDM — one PSG study becomes
   a `visit_occurrence` with per-epoch or per-study `measurement` entries
5. (Stretch) real data: repeat step 3-4 against MIMIC-IV once credentialed,
   compare how much messier a real EHR export is vs. Synthea's clean synthetic
   data

## Layout

```
sql/         # CDM DDL, ETL scripts
notebooks/   # cohort queries, ETL validation
data/        # local Synthea/MIMIC exports (gitignored)
results/     # ETL coverage/validation notes
```

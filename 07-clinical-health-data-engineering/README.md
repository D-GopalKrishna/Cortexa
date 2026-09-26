# Clinical / Health Data Engineering

## ⚠️ Scope note: this track is deliberately narrow

This track is scoped around a short list of applied clinical-data skills
rather than as a survey of the field — it follows the bullets below and
nothing else, so treat it as a focused study path, not a complete picture of
health data engineering.

Skills this track targets:
- Healthcare data standards and formats — EDF/EDF+, DICOM, HL7/FHIR, OMOP/OHDSI
- Large physiological time-series data (EEG, PSG, ECG, actigraphy, wearable streams)
- HIPAA, IRB, and data use agreement (DUA) requirements for human subjects research data
- ML models deployed to production/clinical settings — model serving, monitoring, EHR integration
- Workflow orchestration (Airflow, Prefect, Nextflow, Snakemake, or similar)

## Why this track is different from the rest of the repo

Every other track answers "can you model/decode a neural signal?" This one
answers a completely different question: "can you move that signal through a
real health-data system?" — the standards it must speak (FHIR, OMOP, DICOM),
the governance it must respect (HIPAA/IRB/DUA), and the infrastructure that
gets a model from a notebook into something a clinician's system can call.
None of that is neuroscience — it's data engineering with healthcare-specific
constraints, which is exactly what the skill list above describes.

## Built on existing work, not from scratch

[01-A Sleep stage classification](../01-applied-ml-neuro-data/A-sleep-stage-classification/)
already uses **Sleep-EDF** — real EDF-format PSG data — end to end. That's not
a coincidence to waste: this track's projects are designed to take 01-A's
existing pipeline and push it further through the parts of the stack it
doesn't yet touch (standards conversion, orchestration, deployment), rather
than starting a new domain cold.

## Projects

| # | Project | Core skill | Skill it builds |
|---|---------|-----------|-------------------------------|
| A | [Healthcare data standards interop](A-healthcare-data-standards-interop/) ⭐ starter | EDF/EDF+ parsing, FHIR resource modeling, DICOM basics | Healthcare data standards and formats — EDF/EDF+, DICOM, HL7/FHIR, OMOP/OHDSI |
| B | [OMOP/OHDSI CDM mapping](B-omop-ohdsi-mapping/) | Common Data Model ETL | OMOP/OHDSI; large-scale observational health data |
| C | [Workflow orchestration pipeline](C-workflow-orchestration-pipeline/) | Airflow/Prefect/Snakemake DAGs | Workflow orchestration (Airflow, Prefect, Nextflow, Snakemake, or similar) |
| D | [Clinical ML deployment](D-clinical-ml-deployment/) | Model serving, monitoring, EHR integration | Deploying ML models into production or clinical settings — model serving, monitoring, EHR integration |

## Suggested order

A first (standards literacy + the FHIR/DICOM building blocks C and D both
use) → B and C can run in parallel → D last (needs a served model and,
ideally, C's orchestration wrapped around it).

## Compliance literacy (not a coding project)

HIPAA, IRB, and DUA requirements aren't something you build — they're
something you can speak fluently about and apply correctly. Treat this as a
reading/checklist task rather than a project:

- Read the HHS HIPAA Privacy Rule summary and the Safe Harbor / Expert
  Determination de-identification standards (the two paths to legally
  de-identify health data)
- Read your institution's (or a public university's, e.g. Stanford's) IRB
  guidance on secondary use of human subjects data and what a Data Use
  Agreement typically restricts (re-identification attempts, redistribution,
  storage location)
- Apply it concretely: for whichever public dataset you use in A/B/C/D (even
  if already de-identified), write one paragraph in that project's README on
  what de-identification standard it claims to meet and what a DUA would
  likely restrict if it weren't already public — this is the kind of judgment
  the requirement is actually testing for, not just word recognition

## Shared skills to practice

- Reading and writing FHIR resources (Patient, Observation, DiagnosticReport)
- OMOP CDM table structure (person, visit_occurrence, measurement, concept)
- DAG-based pipeline design: idempotency, retries, backfills, task dependencies
- Model serving basics: a REST endpoint, versioning, and what "monitoring" a
  deployed model actually means (input drift, prediction distribution shift)

# Workflow Orchestration Pipeline

Wrap [01-A Sleep stage classification](../../01-applied-ml-neuro-data/A-sleep-stage-classification/)'s
existing manual pipeline (load -> filter -> features -> train -> evaluate) in
a real orchestration tool, with proper task dependencies, retries, and
backfills — the "workflow orchestration (Airflow, Prefect, Nextflow,
Snakemake, or similar)" requirement, applied to a pipeline that already
exists rather than a toy DAG.

## Why 01-A specifically

It already has clean phase boundaries (`plan/`, `notebooks/` per phase,
`server/` with `data/`, `features/`, `models/`, `eval/`) — that's already
close to a DAG's shape. This project's job is turning "run these notebooks
in order by hand" into "a DAG that knows its own dependencies, can retry a
failed step, and can backfill if new subjects are added."

## Suggested stack (pick one)

- [Prefect](https://www.prefect.io/) — Python-native, least ceremony, good
  first choice if Airflow feels like overkill for a single-machine pipeline
- [Apache Airflow](https://airflow.apache.org/) — the one most likely to
  match what a real team already runs; more setup (scheduler, metadata DB)
- [Snakemake](https://snakemake.readthedocs.io/) — file-dependency-based
  rather than explicit-DAG-based; a very natural fit if the pipeline's stages
  are best expressed as "this file depends on that file" (which 01-A's
  raw -> processed -> features -> model artifact chain already is)

## Milestones

1. Express 01-A's existing pipeline stages as explicit tasks with declared
   dependencies (ingest one subject -> filter -> extract features -> train ->
   evaluate) in the chosen tool
2. Run it end-to-end for one subject; confirm outputs match the original
   notebook-driven results (this is a refactor, not a rewrite — no silent
   behavior change)
3. Parallelize across subjects (the DAG should fan out per-subject
   preprocessing before fanning back in for training) — measure wall-clock
   improvement vs. the sequential notebook version
4. Fault tolerance: kill a task mid-run, confirm the orchestrator retries or
   resumes correctly rather than needing a full manual restart
5. Backfill: add a new subject to the raw data folder, confirm the
   orchestrator can incrementally process just the new subject rather than
   reprocessing everything
6. (Stretch) schedule it (cron-style periodic run) and add basic
   pipeline-level monitoring/alerting on task failure

## Layout

```
dags/ (or Snakefile)   # orchestration definitions
notebooks/             # original 01-A notebooks, kept for output comparison
results/               # runtime comparison (sequential vs. orchestrated), fault-tolerance test notes
```

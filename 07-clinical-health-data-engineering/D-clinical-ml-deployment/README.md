# Clinical ML Deployment

Take a trained model (01-A's sleep-stage classifier, or the disease/region
model from elsewhere in the portfolio) and actually deploy it: a served
endpoint, versioning, monitoring for drift, and a simulated EHR-integration
call pattern — what deploying an ML model into a production or clinical
setting actually involves: model serving, monitoring, and EHR integration.
Everything else in this repo stops at a notebook metric; this is the only
project that asks what happens after the model is "done."

## Why build on existing pieces

[01-applied-ml-neuro-data/showcase](../../01-applied-ml-neuro-data/showcase/)
already has a Flask backend serving portfolio project results — extend that
rather than standing up a second, disconnected backend. The goal is a
realistic serving path, not a new app.

## Suggested stack

- FastAPI (or extend the existing Flask showcase backend) for the serving
  endpoint
- `mlflow` or a simple versioned artifact store for model versioning or
  rollback
- Basic monitoring: log every prediction's input feature summary + output;
  a simple drift check (e.g. population stability index or a KS test between
  training-time and serving-time feature distributions)
- EHR integration simulation: since there's no real EHR to integrate with,
  simulate the call pattern a real integration would use — e.g. accept a
  FHIR `Observation` (using [A](../A-healthcare-data-standards-interop/)'s
  FHIR modeling work) as the input format, return a FHIR-shaped result

## Milestones

1. Serve 01-A's trained sleep-stage classifier behind a REST endpoint;
   confirm predictions match the offline notebook's output exactly (no
   silent preprocessing mismatch between training and serving code)
2. Add model versioning: serve two versions side by side, route a request to
   a specific version, log which version served which prediction
3. Add basic monitoring: log input/output distributions per request; write a
   scheduled (or on-demand) drift check comparing recent serving-time
   feature distributions to the training set's
4. EHR-shaped I/O: accept a FHIR `Observation` as input (reusing
   [A](../A-healthcare-data-standards-interop/)'s FHIR models), return a
   FHIR-shaped `Observation`/`DiagnosticReport` as output, instead of a bare
   JSON array of stage labels
5. (Stretch) wrap the whole serving path in [C](../C-workflow-orchestration-pipeline/)'s
   orchestrator — e.g. a scheduled retraining job that only redeploys a new
   model version if it beats the currently served version on a held-out set

## Layout

```
service/     # serving app (FastAPI or extended showcase/backend)
notebooks/   # drift-check prototyping, version-comparison analysis
results/     # served-vs-offline prediction parity check, drift check output
```

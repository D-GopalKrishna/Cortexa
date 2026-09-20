# Healthcare Data Standards Interop ⭐ starter

Take physiological time-series data already sitting in this repo and push it
through the standards a real clinical data system actually speaks: parse
EDF/EDF+ properly (not just via MNE's convenience loader), model the result
as FHIR resources, and get familiar with DICOM's structure even though this
repo's imaging data (Haxby) isn't DICOM-native.

## Why start here

[01-A Sleep stage classification](../../01-applied-ml-neuro-data/A-sleep-stage-classification/)
already loads Sleep-EDF via MNE, which hides the EDF format's actual
structure (header, signal headers, annotations) behind a clean API. This
project reopens that box, then goes one step further: representing the same
recording as **FHIR** resources, which is the format a real EHR-adjacent
system would expect it in.

## Suggested stack

- `pyedflib` or `edflib-python` — parse EDF/EDF+ directly (headers, per-signal
  sample rates, annotations) instead of through MNE's abstraction
- `fhir.resources` (Python FHIR resource models) or raw JSON against the
  [HL7 FHIR spec](https://www.hl7.org/fhir/) — model an EDF recording as a
  FHIR `Observation` (or `DiagnosticReport` referencing a binary attachment)
- `pydicom` — read a public sample DICOM file (e.g. from
  [pydicom's test data](https://github.com/pydicom/pydicom-data) or a
  public de-identified sample set) to learn DICOM's tag-based structure, even
  without a DICOM dataset elsewhere in this repo

## Milestones

1. Parse one Sleep-EDF file's header and annotations directly with
   `pyedflib` — list every signal, its sample rate, and every annotation
   (sleep stage label) as raw EDF+ structures, no MNE
2. Model that recording as FHIR resources: a `Patient` (synthetic), an
   `Observation` per epoch or a `DiagnosticReport` for the whole study,
   correctly using FHIR's coding systems (e.g. LOINC codes for EEG/PSG study
   types) rather than free-text
3. Round-trip check: from your FHIR JSON, reconstruct enough to re-derive the
   original epoch/label sequence — proves the FHIR model didn't lose
   information the ML pipeline in 01-A actually needs
4. DICOM literacy: load a sample DICOM file with `pydicom`, print its tag
   structure, and write a short comparison note — how DICOM's tag/dataset
   model differs from FHIR's resource/reference model, and why imaging uses
   one and structured clinical data increasingly uses the other
5. (Stretch) Serve the FHIR resources from a minimal FHIR-compliant API
   (e.g. using [HAPI FHIR](https://hapifhir.io/) or a lightweight Python FHIR
   server) so a real FHIR client could query them

## Layout

```
notebooks/   # EDF parsing, FHIR modeling, DICOM exploration
src/         # EDF -> FHIR conversion helpers
data/        # local EDF/DICOM samples (gitignored)
results/     # round-trip validation notes, DICOM-vs-FHIR comparison writeup
```

# Applied ML on Neuro Data

Train classifiers and decoders on public neuroimaging / electrophysiology datasets. Shared pattern: **load → preprocess → features or representation → model → evaluate**.

## Projects

| Project | Dataset | Why it matters |
|---------|---------|----------------|
| [Sleep stage classification](sleep-stage-classification/) ⭐ starter | Sleep-EDF | Cleanest labels; pipeline reuses everywhere |
| [Motor imagery classifier](motor-imagery-classifier/) | PhysioNet EEG Motor Movement/Imagery | Classic BCI ML baseline (CSP+LDA or CNN) |
| [Seizure detection](seizure-detection/) | CHB-MIT Scalp EEG | Strong clinical / resume signal |
| [fMRI cognitive state decoding](fmri-cognitive-state-decoding/) | Haxby | First fMRI project; famous, small |

## Shared skills to practice

- MNE-Python / Nilearn loading and epoching
- Filtering, artifact handling, feature extraction (PSD, bandpower, CSP)
- Subject-wise / session-wise cross-validation (avoid leakage)
- Reporting metrics that matter for clinical / BCI settings (sensitivity, FPR, balanced accuracy)

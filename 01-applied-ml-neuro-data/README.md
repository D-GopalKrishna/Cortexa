# Applied ML on Neuro Data

Train classifiers and decoders on public neuroimaging / electrophysiology datasets. Shared pattern: **load → preprocess → features or representation → model → evaluate**.

## Showcase

A small dashboard (Vite/React/shadcn frontend + Flask backend) with one tab per
project below — see [showcase/](showcase/) to run it locally.

## Projects

| # | Project | Dataset | Why it matters |
|---|---------|---------|----------------|
| A | [Sleep stage classification](A-sleep-stage-classification/) ⭐ starter | Sleep-EDF | Cleanest labels; pipeline reuses everywhere |
| B | [Motor imagery classifier](B-motor-imagery-classifier/) | PhysioNet EEG Motor Movement/Imagery | Classic BCI ML baseline (CSP+LDA or CNN) |
| C | [Seizure detection](C-seizure-detection/) | CHB-MIT Scalp EEG | Strong clinical relevance |
| D | [fMRI cognitive state decoding](D-fmri-cognitive-state-decoding/) | Haxby | First fMRI project; famous, small |
| E | [MEG preprocessing & information retrieval](E-meg-preprocessing-information-retrieval/) | MNE sample / OpenNeuro MEG | Sensor cleaning → evoked / decode pipeline |
| F | [Disease vulnerability × gene expression](F-disease-vulnerability-gene-mapping/) | Allen Human Brain Atlas + GWAS Catalog | No lab needed; asks why diseases pick the regions they pick |
| G | [In-vivo awake-behaving decoding](G-invivo-awake-behaving-decoding/) | IBL / Allen Neuropixels (real spikes) | Closest software-only substitute for in-vivo/awake-behaving experience |

## Shared skills to practice

- MNE-Python / Nilearn loading and epoching
- Filtering, artifact handling, feature extraction (PSD, bandpower, CSP)
- Subject-wise / session-wise cross-validation (avoid leakage)
- Reporting metrics that matter for clinical / BCI settings (sensitivity, FPR, balanced accuracy)

# Datasets

## Primary (v1 — use these first)

### Sleep-EDF / Sleep-EDF Expanded (PhysioNet)
- 197 PSG recordings total: 153 "Sleep Cassette" (78 healthy subjects, ages 25–101) +
  44 "Sleep Telemetry" (22 subjects, temazepam study). Full dataset is **~8.1 GB**;
  Sleep Cassette alone is roughly **6–6.5 GB**.
- 2 EEG channels (Fpz-Cz, Pz-Oz), 1 EOG, 1 chin EMG, 100 Hz sampling, 30s epochs.
- **Scored under the older 1968 Rechtschaffen & Kales (R&K) rules, not modern AASM**
  — a real difference from most newer datasets, worth knowing before comparing
  numbers against a paper that used AASM-scored data. Single expert scorer per
  recording (not double-scored); inter-rater agreement between two human scorers on
  sleep staging generally tops out around ~83%, so this — like any single-scored
  dataset — has some irreducible label noise baked into "ground truth."
- Includes `?` (unscored) and `Movement` epochs that must be explicitly filtered out
  during preprocessing, not silently mapped to a real stage label.
- https://www.physionet.org/content/sleep-edfx/
- **Start with Sleep Cassette only** (not the full 197): smallest footprint, free
  with no application process, and — genuinely the deciding factor — the
  best-documented option available. MNE-Python ships an official tutorial for it
  (`60_sleep.html`) plus community starter notebooks, so the "how do I load this"
  problem is largely solved already. It's also what nearly every paper in
  [03-model-landscape.md](03-model-landscape.md) benchmarks against, so results stay
  comparable to the literature.

## Is data availability actually a blocker?

No. The 20–50-dataset scale of SLEEPYLAND/OmniEEG-Bench/NeuroAtlas is a
generalization-robustness test (EEG hardware/montage/population/labeling protocol
vary a lot across labs), not a sign that good EEG data is scarce. Sleep-EDF alone is
the standard benchmark in hundreds of published papers and is genuinely sufficient
for this project; SHHS/MASS/ISRUC below already give real cross-dataset testing at
portfolio scale without needing anywhere near that many sources.

### Easy-access sources (no lengthy DUA — worth knowing about even if unused)

- **Kaggle**: mostly community re-uploads of PhysioNet data (e.g.
  `iamommpatel/physiobank-database-sleep-edfx-cassette` mirrors Sleep-EDF; several
  CHB-MIT seizure-EEG mirrors exist too). Convenient, zero signup friction, but
  documentation/licensing is inconsistent — treat as a mirror, verify against the
  PhysioNet original before relying on one. The "Grasp-and-Lift EEG Detection" (2015)
  competition is a solid motor-imagery-adjacent dataset if that direction comes up
  later (see [B-motor-imagery-classifier](../B-motor-imagery-classifier/)).
- **OpenNeuro** (no DUA at all, instant download, BIDS-formatted): **Bitbrain Open
  Access Sleep (BOAS)** — 128 nights, PSG + wearable EEG headband, human-consensus
  labels (`openneuro.org/datasets/ds005555`); **EESM19** — 20 subjects, home PSG +
  ear-EEG. Both good, easy secondary/tertiary options alongside SHHS/MASS/ISRUC.
- **PhysioNet eegmmidb** — 109 subjects, 64-channel motor movement/imagery, not
  sleep-relevant but useful if this pipeline gets reused for
  [B-motor-imagery-classifier](../B-motor-imagery-classifier/).
- **TUEG (Temple University EEG Corpus)** — largest open EEG corpus (30,000+
  recordings), access needs a signed form emailed to NEDC (days, not the weeks a
  clinical DUA takes) — relevant mainly if pretraining a foundation model from
  scratch in Phase 8, not for the core sleep-staging phases.

## Secondary (generalization / v2)

**Why not start with more than one dataset?** This was researched, not assumed: the
literature on cross-dataset generalization (RobustSleepNet, MEASURE, and similar)
confirms models really do overfit to one dataset's hardware/montage/scoring
idiosyncrasies — that's a genuine effect, not caution for its own sake. But it's a
concern to address *after* a pipeline works end-to-end on one dataset, not before.
Pulling in a second dataset from day one mostly adds engineering overhead
(reconciling different montages, sampling rates, scoring conventions) before the
basics are validated. Standard sequencing — and what this plan follows — is one
dataset first (Sleep-EDF, Phases 0-8), a second only once there's something working
to test generalization with (Phase 9).

### ISRUC-Sleep — recommended second dataset
- Three subgroups: 100 subjects (1 session), 8 subjects (2 sessions, for
  reproducibility), 10 healthy subjects. From Hospital of Coimbra University,
  double-scored by two human experts (stronger label quality than Sleep-EDF's
  single-scorer setup). Includes healthy, disordered, *and medicated* subjects.
- https://sleeptight.isr.uc.pt — free download via MEGA links, no application
  process, same low friction as Sleep-EDF. This is why it's the recommended Phase 9
  starting point over SHHS/MASS below.
- Use for: deliberately non-clean data — disorders and medication effects that
  Sleep-EDF's mostly-healthy cohort doesn't cover.

### SHHS — Sleep Heart Health Study
- Large multi-center cohort (~6,441 subjects, ~5,793 with raw PSG at Visit 1),
  originally studying sleep-disordered breathing and cardiovascular disease. Home
  unattended PSG. EEG 125 Hz (C3/A2, C4/A1), EOG 50 Hz, EMG 125 Hz.
- Distributed via NSRR (National Sleep Research Resource); a 1,000-record subset is
  also on PhysioNet. **Requires an application/approval process** (free, but real
  friction, unlike ISRUC) — hundreds of GB if pulled in full.
- Use for: scale, and testing whether a model trained on Sleep-EDF generalizes to a
  much larger, more clinically heterogeneous population — once ISRUC's lower-friction
  generalization check is already done.

### MASS — Montreal Archive of Sleep Studies
- 200 subjects, 5 subsets (SS1–SS5) pooled from multiple hospital sleep labs, scored
  per AASM (SS1, SS3) or R&K (SS2/SS4/SS5). SS3 (62 subjects, 20-channel EEG) is the
  subset most used in ML papers.
- https://borealisdata.ca/dataverse/MASS — **requires institutional ethics approval
  and a request to the CÉAMS team**, more friction than SHHS's NSRR application.
- Use for: multi-channel EEG (unlike Sleep-EDF's 2 channels), useful once you want to
  explore montage/channel-selection questions.

### DREAMT (PhysioNet, 2024) — newer, worth knowing about
- 100 subjects, full clinical PSG + Empatica E4 wearable, expert-annotated 30s
  epochs. Modern and well-documented, but not specially "pre-cleaned" — the dataset
  page is explicit that only minimal resampling was applied, no ML-readiness claims
  beyond that.
- https://physionet.org/content/dreamt/
- Use for: if a wearable-vs-clinical-PSG comparison becomes interesting later
  (adjacent to the Phase 8 efficiency/deployment angle) — not a priority pull.

## Out-of-domain generalization benchmark (2025)

### SLEEPYLAND
- Rossi, Metaldi, Bechny et al., *npj Digital Medicine* 9:55 (2025), arXiv 2506.08574.
  Open-source Python toolbox for **fair, standardized evaluation** of automatic
  sleep-staging models across many datasets at once — aggregates ~220,000 hours
  in-domain PSG (17 NSRR datasets) + ~84,000 hours out-of-domain (7 datasets,
  including Bern Sleep-Wake Registry, DOD-H, DOD-O), spanning diverse ages, disorders,
  and recording hardware.
- GitHub: `biomedical-signal-processing/sleepyland`
- **Correction to note**: SOMNUS is not a separate dataset. It's the ensemble model
  introduced *inside* the SLEEPYLAND paper — a soft-voting ensemble of several
  pretrained sleep-staging models, evaluated across 24 datasets (macro-F1 68.7–87.2%),
  and on multi-annotated data it beats the best individual human scorer (85.2% vs
  80.8% macro-F1 on one dataset). Both names are real; they come from the same paper.
- Use for: Phase 7 (generalization). This is the right place to test a model trained
  on Sleep-EDF against genuinely out-of-domain recordings without hand-rolling a
  cross-dataset eval pipeline yourself.

### U-Sleep (Perslev et al., npj Digital Medicine 2021)
- Earlier generalization-focused precedent, successor to U-Time, explicitly built and
  evaluated for resilience across many heterogeneous PSG datasets. Worth reading
  alongside SLEEPYLAND for how the field approached this before SLEEPYLAND formalized
  it as a benchmark.

### OmniEEG-Bench
- Lu, Li, Shen et al. (SUSTech NCC Lab), arXiv 2606.00815 (2026). *"OmniEEG-Bench: A
  Standardized Evaluation Benchmark for EEG Foundation Models."*
- Benchmarks 10 EEG foundation models across 54 unified EEG datasets, organized into 6
  task families (signal reliability; biometrics/disease; consciousness/state;
  cognition/emotion; naturalistic stimulus decoding; motor/interaction) via a
  standardized "task-card" spec. Finds pretraining-data diversity and model size both
  correlate with better cross-dataset rank.
- Code: `github.com/ncclab-sustech/omni-eegbench`
- Broader than sleep staging specifically — use this in Phase 8 to sanity-check how
  the foundation model you fine-tune (BIOT/LaBraM/etc.) is reported to generalize
  across task families, not just on sleep data.

### NeuroAtlas
- Kontras, Osselaer, Mouslech et al. (KU Leuven / MIT), arXiv 2605.14698 (2026).
  *"NeuroAtlas: Benchmarking Foundation Models for Clinical EEG and
  Brain-Computer Interfaces."*
- **Note**: despite the name, this is a benchmark suite, not a connectomics brain
  atlas (unrelated to the "atlas" usage in [04-connectomics/](../../04-connectomics/)).
- Benchmarks 20 models (29 size variants) — EEG foundation models (BIOT, CBraMod,
  EEGPT, LaBraM, NeuroLM, REVE, SleepFM) plus generic time-series models — across 42
  datasets (~260k hours) spanning seizure detection, sleep staging/event
  detection/diagnosis, brain-age estimation, and BCI.
- Key finding worth carrying into Phase 8: specialized "brain-wave" EEG foundation
  models largely *underperform* generic time-series models; no model yet delivers an
  out-of-the-box unified EEG solution; rankings shift substantially across datasets.
  This directly reinforces the caveat already noted in
  [03-model-landscape.md](03-model-landscape.md) — treat it as corroborating
  evidence, not a surprise, when Phase 8's own fine-tuning results are inconclusive.
- Directly includes sleep staging as one of its 4 domains (via SleepFM as a named
  baseline) — closer to a direct analog of SLEEPYLAND than OmniEEG-Bench is.

## Notes

- Start with Sleep-EDF alone through Phase 6. Bring in SHHS/MASS/ISRUC/SLEEPYLAND only
  in Phase 7, once there's a trained model worth stress-testing.
- OmniEEG-Bench and NeuroAtlas are Phase 8 tools (foundation-model evaluation), not
  Phase 7 tools (they benchmark pretrained models against each other, not your
  from-scratch models against new datasets) — see [04-phases.md](04-phases.md).
- All raw data goes in `data/raw/` (gitignored) — never commit PSG recordings.

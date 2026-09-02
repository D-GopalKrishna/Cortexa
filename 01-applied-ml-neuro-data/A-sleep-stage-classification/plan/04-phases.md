# Phase-by-phase build plan

Each phase has a notebook for exploration and, once the approach is settled, a
matching module under `server/`. Every phase ends with the same three headline metrics
(accuracy, macro F1, Cohen's kappa) **plus per-stage precision/recall/F1 and a
confusion matrix**, logged to `results/comparison.csv` so the table grows across the
whole project. Each phase also has an explicit "definition of done" — don't move on
until it's checked off; this is what keeps a 10-phase plan from turning into 10
half-finished notebooks.

## Phase 0 — Environment & data setup
- Set up Python env (MNE, NumPy, SciPy, scikit-learn, PyTorch, XGBoost); pin versions
  in `requirements.txt` / `environment.yml` — reproducibility starts here, not at the
  end.
- Fix all random seeds (numpy, torch, python `random`) in `server/utils/config.py` and
  reuse the same seeding call everywhere. Log the seed alongside every result row.
- **Dataset decision (researched, not assumed)**: download only **Sleep-EDF's "Sleep
  Cassette" subset** (153 recordings, 78 healthy subjects, ~6-6.5 GB) to start —
  smallest footprint, zero access friction (open on PhysioNet, no application), and
  the best-documented option (MNE ships an official tutorial for it). Do **not** pull
  in a second dataset yet — that's deliberate, not an oversight: models trained on
  one dataset genuinely do overfit to its hardware/montage/scoring quirks (a real,
  literature-backed effect — see RobustSleepNet, MEASURE), but that's a
  generalization concern to address once a pipeline works, not before. A second
  dataset (ISRUC — also frictionless, free download, no application) belongs in
  Phase 9, exactly where it already sits.
- Two known data quirks to handle explicitly in the download/loading step, not
  discover later: Sleep-EDF is scored under the older 1968 R&K rules (not modern
  AASM) and includes `?` (unscored) and `Movement` epochs — filter these out rather
  than silently mismapping them to a real stage label.
- `server/data/download.py`: fetch a small Sleep Cassette subject subset (start with
  ~10-20 subjects, not all 153) via MNE's built-in fetcher or PhysioNet directly.
- `notebooks/01_explore_sleepedf.ipynb`: load one subject, plot raw EEG + hypnogram,
  sanity-check channel names/sampling rate/epoch alignment, and confirm `?`/Movement
  epochs are being dropped correctly.
- **Definition of done**: raw data loads deterministically from a fresh clone given
  only `requirements.txt` + the download script; one subject's signal and hypnogram
  visually verified against PhysioNet's own documentation; unscored/movement epochs
  confirmed excluded from the label set.

## Phase 1 — Exploratory data analysis & data quality
*(new — worth its own phase rather than folding into preprocessing)*
- `notebooks/01b_eda.ipynb`: class balance per subject and pooled (expect heavy N2
  skew, thin N1); epoch counts per recording; missing/short recordings; channel
  quality checks (flatlines, extreme amplitude, saturation).
- Stage-transition analysis: build a transition matrix (P(stage[t+1] | stage[t])) —
  this motivates why sequence models (Phase 5) should help, and gives a concrete
  number to point back to later rather than an assumed claim.
- Document findings in `plan/05-eda-findings.md` (create when EDA is run) so later
  phases can cite specific numbers instead of re-deriving them.
- **Definition of done**: a class-imbalance number and a transition matrix exist and
  are referenced by name in Phase 3+'s loss-function choices.

## Phase 2 — Preprocessing pipeline
- `server/data/preprocessing.py`: bandpass filter, epoch segmentation (30s windows
  aligned to hypnogram labels), artifact/quality checks flagged in Phase 1.
- `server/data/loaders.py`: subject-wise train/val/test split utility — reusable by
  every later phase so the split is always identical and comparable. Fix the actual
  subject-ID split list in a checked-in file (e.g. `configs/splits.json`), not
  regenerated per run, so every phase's numbers are on the *exact* same test set.
- Add a `server/data/leakage_check.py` sanity test: assert no subject ID appears in more
  than one of train/val/test. Run this as an actual test, not a manual glance.
- Output: a `data/processed/` cache (e.g. epochs + labels as numpy arrays or an MNE
  Epochs object) that every later phase loads instead of re-parsing raw EDF files.
- **Definition of done**: the leakage check passes as an automated assertion, and the
  split file is committed so results are reproducible by anyone re-running the repo.

## Phase 3 — Classical baseline
- `server/features/spectral.py`: bandpower per canonical band, per epoch, per channel.
- `server/features/statistical.py`: the multi-domain feature set (variance, skewness,
  kurtosis, Higuchi fractal dimension, permutation entropy, spectral edge frequency)
  described in [03-model-landscape.md](03-model-landscape.md).
- `notebooks/02_features_classical.ipynb`: train Logistic Regression, Random Forest,
  and XGBoost; report per-stage F1 and confusion matrix for all three, not just the
  winner — the *comparison* is the point of this phase, not just the best number.
- **Class imbalance handling as a deliberate ablation**: compare class weights vs.
  SMOTE-style oversampling vs. no correction, and report the effect on N1 recall
  specifically (the stage this dataset punishes most). Pick one approach and carry
  it forward; note the choice in the results table.
- **Feature importance**: XGBoost/RF feature importances or SHAP values — which
  bands/features actually drive predictions? This is a genuinely interpretable
  result worth a portfolio figure, and a real check against domain knowledge (delta
  power should dominate for N3, for instance — if it doesn't, that's worth
  investigating before moving on).
- **Definition of done**: three classical models compared on identical features and
  splits, one imbalance-handling strategy chosen with evidence, one feature
  importance figure produced. This phase's numbers are the floor every later model
  must beat.

## Phase 4 — Deep learning baseline (DeepSleepNet-style)
- `server/models/deepsleepnet.py`: CNN feature extractor + BiLSTM, trained on raw
  single-channel EEG.
- `notebooks/03_deep_baselines.ipynb`: training loop, learning curves (train vs. val
  loss, watch for overfitting given how small a 10-20 subject Sleep-EDF subset is),
  compare against Phase 3.
- **Class-imbalance loss ablation carried forward from Phase 3**: try weighted
  cross-entropy and focal loss here too — deep models and classical models often
  respond differently to the same imbalance-handling trick, worth re-checking rather
  than assuming Phase 3's answer transfers.
- **Definition of done**: a trained CNN+BiLSTM with documented learning curves,
  compared against Phase 3 on the same metrics — first real test of "does raw-signal
  deep learning beat handcrafted features here," reported honestly either way.

## Phase 5 — Sequence models
- `server/models/seqsleepnet.py`: hierarchical RNN operating on a *sequence* of epochs
  rather than one at a time.
- `notebooks/04_sequence_models.ipynb`: quantify the gain from sequence context vs.
  Phase 4's single-epoch model, especially on ambiguous transition epochs — use the
  Phase 1 transition matrix to identify which specific transitions (e.g. N1↔Wake,
  N1↔REM) improve most.
- **Sequence-length ablation**: try at least 2-3 context-window sizes (e.g. 5, 10, 20
  epochs) and report how accuracy/kappa change — "more context always helps" is a
  claim worth actually testing, not assuming.
- **Definition of done**: sequence model beats or is honestly compared against Phase
  4, with a sequence-length ablation table and a specific transition-type breakdown.

## Phase 6 — Attention / transformer models
- `server/models/attnsleep.py` and `server/models/sleeptransformer.py`.
- `notebooks/05_attention_transformer.ipynb`: train both, and specifically inspect
  SleepTransformer's attention heatmaps — visualize what the model is attending to
  for a few example epochs, especially misclassified N1 epochs. This interpretability
  angle is worth a portfolio figure on its own.
- **Uncertainty/calibration check**: SleepTransformer supports uncertainty
  quantification natively — compare predicted confidence on correct vs. incorrect
  epochs (a reliability diagram). A model that's confidently wrong is a worse
  clinical tool than one that's honestly unsure, and this is a cheap, high-value
  figure to add here.
- **Definition of done**: both models trained and compared, one attention-heatmap
  figure, one calibration/reliability figure.

## Phase 7 — Error analysis
*(new — a dedicated phase rather than an aside)*
- `notebooks/06_error_analysis.ipynb`: pool misclassifications across every model
  trained so far. Which epochs does *every* model get wrong (likely genuinely
  ambiguous, possibly worth a manual relisten/relabel spot-check against the raw
  signal)? Which epochs does only the classical baseline get wrong but every deep
  model gets right (this is the concrete "why deep learning helped" evidence)?
- Per-subject error breakdown: is error uniform across subjects, or do a few
  subjects (older age, unusual physiology) drag down the pooled numbers? This
  matters for the generalization story in Phase 10.
- **Statistical significance**: use McNemar's test (or a bootstrap CI on the metric
  differences) when comparing two models' errors on the *same* test set — a 1-2%
  accuracy gap between two models is not automatically meaningful, and this phase is
  where that gets checked rather than assumed.
- **Definition of done**: a written summary of *why* errors happen (not just where),
  with at least one statistical significance comparison between two adjacent-phase
  models.

## Phase 8 — Efficiency & deployment
- `server/models/tinysleepnet.py`.
- `notebooks/07_efficiency_deployment.ipynb`: compare every model trained so far on
  accuracy **vs. parameter count vs. inference latency** (CPU-only timing per epoch,
  and per full-night sequence). Produce a Pareto-style plot: this is the figure that
  makes "efficiency is a different optimization target" concrete rather than
  asserted.
- **Model export**: export at least one model (likely TinySleepNet) to ONNX or
  TorchScript, and re-benchmark latency on the exported format vs. native PyTorch —
  this is what actually makes deployment/serving (Phase 11) possible rather than
  theoretical.
- **Definition of done**: a Pareto plot, and one exported model artifact that loads
  and predicts correctly outside the training notebook.

## Phase 9 — Generalization / out-of-domain evaluation
- Bring in SHHS, MASS, ISRUC and/or the SLEEPYLAND benchmark toolbox (see
  [02-datasets.md](02-datasets.md)).
- `notebooks/08_generalization_eval.ipynb`: take the best model(s) from Phases 3-8,
  trained only on Sleep-EDF, and evaluate zero-shot on the other datasets. Expect a
  real accuracy drop — quantify it per stage, and connect it back to the Phase 7
  per-subject error analysis (does the gap track with the kind of subject variation
  already seen in-domain, or is it a genuinely new failure mode from different
  hardware/montage?).
- Optionally reproduce a small piece of the SOMNUS ensemble idea (soft-voting across
  your own Phase 3-8 models) and see if it recovers some of the generalization gap.
- **Definition of done**: an in-domain vs. out-of-domain metrics table, with a
  specific hypothesis (not just a number) for why the gap is the size it is.

## Phase 10 — Foundation models / transfer learning
- Pick one pretrained EEG foundation model with available weights (BIOT and LaBraM
  both have public checkpoints; check EEGPT/CBraMod/Brant-2 availability at
  implementation time — some are recent enough that weights may not be public yet).
- `notebooks/09_foundation_models.ipynb`: fine-tune on Sleep-EDF, compare directly
  against the from-scratch Phase 4-8 models on the *same* split and metrics.
- The interesting result here isn't "foundation model wins" — it's whether it wins,
  by how much, and whether that's worth the extra compute/complexity. Report
  honestly per the caveat in [03-model-landscape.md](03-model-landscape.md).
- Cross-check your own fine-tuning result against the two standardized benchmark
  papers in [02-datasets.md](02-datasets.md): **OmniEEG-Bench** (10 EEG-FMs across 54
  datasets/6 task families) and **NeuroAtlas** (20 models across 42 clinical
  datasets, sleep staging included via SleepFM). NeuroAtlas's headline finding —
  specialized EEG foundation models often underperform generic time-series models —
  is a useful prior to hold before concluding your own fine-tune result is anomalous
  either way.
- **Definition of done**: a fine-tuned foundation model with a head-to-head
  comparison against the best from-scratch model, and an honest verdict on whether
  it was worth it.

## Phase 11 — Serving & the showcase app
*(new)*
- Wrap the best-performing exported model (Phase 8's ONNX/TorchScript artifact, or
  simply the best `.pt`/`.pkl` if export wasn't taken further) behind a small
  inference function: `server/eval/predict.py`, taking a raw EDF (or a pre-extracted
  epoch array) and returning per-epoch stage predictions + confidence.
- This is what the Flask backend in `01-applied-ml-neuro-data/showcase/backend/`
  calls for this project's tab — see the top-level showcase app (sibling to this
  project, one level up) for the shared dashboard all 5 projects plug into.
- Minimum viable demo: upload or pick a held-out sample recording → show the
  predicted hypnogram next to the true one → show accuracy/kappa for that one
  recording. Doesn't need to be fancier than that to be a legitimate portfolio demo.
- **Definition of done**: a working prediction endpoint this project owns, callable
  from the showcase backend, returning a hypnogram-shaped prediction for at least one
  held-out recording end to end.

## Phase 12 — Synthesis
- Final comparison table + Pareto plot (accuracy vs. compute) across every phase.
- Write-up: what each architectural jump actually bought, in your own reproduced
  numbers, not just cited paper numbers — pull directly from the Phase 7 error
  analysis and Phase 9 generalization gap rather than re-deriving conclusions here.
- Portfolio figures: hypnogram overlay (true vs. predicted), confusion matrices,
  attention heatmap example, calibration/reliability diagram, efficiency Pareto plot,
  in-domain vs. out-of-domain comparison.
- Feed the write-up and figures into the showcase app's tab for this project.

## Sequencing notes
- Phases 0-3 are the minimum viable v1 mentioned in the original README — get there
  first, working end to end, before adding architectural sophistication.
- Phases 4-8 can be reordered or trimmed if time is limited; each is self-contained
  given Phase 2's processed data cache. Phase 7 (error analysis) is cheap relative to
  training a new model and is worth doing even under time pressure — it's what turns
  a metrics table into an actual understanding of the problem.
- Phases 9-10 assume Phases 0-8 are done and produce real numbers to compare against
  — don't skip ahead to foundation models without a from-scratch baseline in hand.
- Phase 11 (serving) can start as soon as *any* model from Phase 3 onward is good
  enough to demo — it doesn't need to wait for Phase 10. Wire up the classical
  baseline to the showcase app early, then swap in better models as later phases
  land, rather than leaving serving until everything else is "done."

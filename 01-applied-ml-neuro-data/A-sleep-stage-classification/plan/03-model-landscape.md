# Model landscape

Verified against the literature (see research notes below each entry). A couple of
names from the original brain-dump came in slightly garbled — corrected inline.

## Classical ML baseline

### XGBoost + multi-domain features
- Genre of paper, not one canonical reference — several near-identical studies exist,
  e.g. "An Effective and Interpretable Sleep Stage Classification Approach Using
  Multi-Domain EEG and EOG Features" (MDPI *Bioengineering* 12(3):286, 2025).
- Approach: two-step feature selection (F-score pre-filter + XGBoost importance
  ranking) over spectral/statistical/entropy features — PSD, SVD entropy, Higuchi
  fractal dimension, DFA, permutation entropy — from EEG+EOG. Reported accuracy
  ~84–91% on Sleep-EDF(x) depending on exact pipeline.
- Role in this plan: Phase 2, alongside plain Logistic Regression / Random Forest on
  bandpower features. This is the ceiling for "features + gradient boosting" before
  we move to learned representations.

## Deep learning evolution

| Model | Year / venue | Key idea |
|---|---|---|
| **DeepSleepNet** | Supratak et al., 2017, IEEE TNSRE | Raw single-channel EEG. Dual-branch CNN (fine + coarse temporal filters) + bidirectional LSTM with residual connections. Two-stage training. ~82% accuracy on Sleep-EDF. Historical starting point of the field. |
| **U-Time** | Perslev, Jensen, Darkner, Jennum, Igel, NeurIPS 2019 | Fully convolutional, U-Net-style segmentation applied to sleep staging — classifies every timepoint then aggregates. Avoids RNN tuning fragility; notably robust across datasets without architecture changes. Successor: **U-Sleep** (2021), explicitly built for cross-dataset generalization. |
| **IITNet** | Seo, Back, Lee, Park, Kim, Lee, 2020, Biomedical Signal Processing and Control (arXiv 1902.06562) | "Intra- and Inter-epoch Temporal Context Network" — residual CNN encodes sub-epoch features, BiLSTM captures context both within and across epochs. End-to-end, no handcrafted features. |
| **SeqSleepNet** | Phan, Andreotti, Cooray, Chén, De Vos, 2019, IEEE TNSRE 27(3):400-410 | Hierarchical RNN, sequence-to-sequence — classifies a whole sequence of epochs at once rather than one at a time. Filterbank layer + attention-based epoch-level RNN + sequence-level RNN. |
| **XSleepNet** | Phan et al., 2021 (arXiv 2007.05492) | Multi-view: fuses raw-signal and spectrogram branches via gradient blending, rather than committing to one input representation. |
| **TinySleepNet** | Supratak & Guo, 2020, IEEE EMBC | Lightweight DeepSleepNet — CNN feature extractor + single LSTM, bypass branch removed. Built for portable/wearable deployment, far fewer parameters. This is the efficiency-phase reference model. |

## Attention / transformer era

| Model | Year / venue | Key idea |
|---|---|---|
| **AttnSleep** | Eldele et al., 2021, IEEE TNSRE | Single-channel EEG. Multi-resolution CNN (MRCNN) + adaptive feature recalibration (AFR) + multi-head-attention temporal context encoder (TCE); class-aware cost-sensitive loss for stage imbalance. |
| **SleepTransformer** | Phan et al., IEEE TBME 69(8):2456-2467, 2022 (arXiv 2105.11043) | Pure Transformer, no CNN/LSTM. Operates on time-frequency images, two-level Transformer (epoch + sequence). Built-in interpretability (attention heatmaps) and uncertainty quantification — worth studying even beyond its accuracy numbers. |
| **SalientSleepNet** | Jia et al., IJCAI 2021 (arXiv 2105.13864) | U²-Net-style multimodal saliency detection applied to sleep staging. |
| **SleePyCo** | 2022/2023 (arXiv 2209.09452) | Feature Pyramid + supervised contrastive learning, single-channel EEG. Strong on the historically hard stages (N1, REM). |
| **L-SeqSleepNet** | Phan, Lorenzen et al., 2023, IEEE TNSRE (arXiv 2301.03441) | **Correction**: this is what "LCQuins sleep net 2023" most likely referred to — a mishearing/mis-transcription. Extends SeqSleepNet to model the ~90-minute sleep cycle directly ("whole-cycle long sequence modelling"); tested across scalp PSG, in-ear EEG, and cEEGrid single-channel setups. |

## Foundation models (EEG-pretrained, self-supervised — not language models)

| Model | Year / venue | Pretraining approach | Sleep-staging evidence |
|---|---|---|---|
| **EEGPT** | NeurIPS 2024 (~10M param version) and a separate, later autoregressive ICLR 2025 submission (up to 1.1B params) — two distinct papers share this name, be careful which one a source means | Mask-based dual self-supervised learning (2024 version) or next-signal-prediction autoregressive pretraining (2025 version) | Evaluated on general BCI downstream tasks; not confirmed with sleep-staging-specific numbers in what was researched — treat as a fine-tuning experiment, not a known benchmark to replicate. |
| **Brant-2** | 2024 (arXiv 2402.10251) | Extends Brant (NeurIPS 2023, intracranial-only) to scalp EEG too. >1B params, pretrained on ~4TB / ~40,000 hours from 15k+ subjects. Mask-prediction + forecasting objectives. | General brain-signal foundation model; no sleep-staging-specific benchmark found. |
| **CBraMod** | 2024/2025, ICLR 2025 (arXiv 2412.07236) | "Criss-Cross" Transformer separating spatial (cross-channel) and temporal (within-channel) attention. Pretrained on the cleaned TUEG corpus. | Evaluated across 10 diverse BCI downstream tasks; sleep-staging inclusion not explicitly confirmed — flag for follow-up when you get here. |
| **BIOT** | NeurIPS 2023 | Tokenizes each channel into fixed-length segments, rearranges into a long "sentence" with channel + relative position embeddings. Handles mismatched channels/lengths/missing values across EEG, ECG, activity data. | Used as a comparison baseline in several downstream EEG papers including some sleep-staging comparisons, per survey literature — no single canonical number found to cite directly. |
| **LaBraM** | ICLR 2024 (spotlight) | Vector-quantized neural tokenizer (VQ-NSP) converts raw EEG patches to discrete codes; Transformer pretrained via masked-code prediction. ~2,500 hours from ~20 datasets. | Same caveat as BIOT — common FM baseline, not independently pinned to a sleep-staging leaderboard here. |

**Honest caveat worth carrying into Phase 8**: a 2025 survey ("EEG Foundation Models:
Progresses, Benchmarking, and Open Problems," arXiv 2601.17883) notes that
general-purpose time-series foundation models (e.g. TimesNet) sometimes *outperform*
EEG-specific foundation models on sleep-stage classification after fine-tuning. Don't
assume a bigger/newer pretrained model automatically wins — that's exactly the
experiment Phase 8 exists to run.

## What we're deliberately not chasing

Chasing the single best-published accuracy number isn't the goal — the goal is
understanding *why* each architectural jump happened (what specific weakness it
addressed) and having your own honest, reproduced numbers for each step. A model in
this list scoring 1-2% higher than another in its original paper is not, by itself, a
reason to skip a phase.

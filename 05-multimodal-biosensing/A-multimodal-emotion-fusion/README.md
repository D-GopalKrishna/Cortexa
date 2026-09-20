# Multimodal Emotion / State Fusion (Galea-style)

Estimate emotional/cognitive state (valence/arousal, or a stress proxy) from
multiple simultaneously-recorded physiological channels, and measure whether
fusing them actually beats the best single modality — the core bet behind
OpenBCI's Galea headset (EEG + EMG + EDA + PPG + eye tracking fused into one
real-time state estimate for VR). This project answers the same question
offline, on a public dataset, with no hardware required.

## Dataset

- [DEAP](https://www.eecs.qmul.ac.uk/mmv/datasets/deap/) — 32 subjects, 32-channel EEG
  + peripheral signals (EOG, EMG, GSR/EDA, respiration, temperature, blood volume
  pulse) recorded while watching 40 one-minute music videos, labeled with
  self-reported valence/arousal/dominance/liking
- Alternative / follow-up: [WESAD](https://ubicomp.oru.se/wesad/) (chest+wrist
  wearable: EDA, ECG, EMG, respiration — no EEG, but cleaner stress labels) if
  you want a second dataset to check generalization

## Why this one

Closest public analog to Galea's actual sensor mix (brain + muscle + skin +
cardiovascular), with a clear, previously-published task (valence/arousal
classification) so you have a baseline to compare against.

## Suggested stack

- Python, MNE (EEG), NeuroKit2 (EDA/ECG/EMG feature extraction — phasic/tonic
  EDA decomposition, HRV, muscle envelope)
- scikit-learn for per-modality baselines; PyTorch for a learned fusion layer
  if the classical fusion methods plateau

## Milestones

1. Load one subject; align all modalities onto a common epoch grid (DEAP is
   pre-segmented per trial, but sample rates differ per channel type)
2. Per-modality feature extraction: EEG bandpower (theta/alpha/beta ratios),
   EDA phasic peaks, EMG envelope, HRV from BVP
3. Single-modality baselines: train a classifier per modality on
   valence/arousal (high/low binary split), report accuracy per modality
4. Early fusion: concatenate all modality features into one classifier;
   compare against the best single modality
5. Late fusion: per-modality classifiers combined by averaging/voting/stacking;
   compare against early fusion
6. Ablation table: every modality-subset combination, to see which channels
   are actually carrying signal vs. adding noise
7. (Stretch) subject-independent split (train/test on disjoint subjects) —
   much harder than within-subject, but closer to a real product setting
8. (Stretch) repeat the fusion comparison on WESAD's stress labels to check
   the "fusion beats best single modality" finding generalizes across tasks

## Layout

```
notebooks/   # one per phase — exploration
src/         # loading, per-modality feature extraction, fusion models
data/        # local dataset (gitignored)
figures/     # per-modality vs. fusion accuracy comparison plots
results/     # ablation table, metrics across fusion strategies
```

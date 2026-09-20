# Multimodal Biosensing

Fuse multiple physiological channels (brain + body) into one state estimate —
the same bet OpenBCI's **Galea** headset makes (EEG + EMG + EDA + PPG + eye
tracking in one device for real-time cognitive/emotional state). No headset
needed: public datasets already recorded several of these modalities together
on real subjects, so the interesting question — does fusing modalities beat
the best single one? — is fully answerable offline.

## Projects

| # | Project | Dataset | Why it matters |
|---|---------|---------|-----------------|
| A | [Multimodal emotion/state fusion](A-multimodal-emotion-fusion/) ⭐ starter | DEAP (EEG + EOG + EMG + GSR + respiration) | Directly mirrors Galea's sensor mix and fusion premise |

## Shared skills to practice

- Aligning signals recorded at different sample rates onto one epoch grid
- Per-modality feature extraction (EEG bandpower, EDA phasic/tonic decomposition, EMG envelope, HR/HRV from PPG or ECG)
- Early fusion (concatenate features) vs. late fusion (per-modality classifiers + a combiner) vs. learned fusion (small fusion network)
- Ablations: single-modality baselines vs. every fusion combination, to see which channels actually carry the signal

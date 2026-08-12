# Motor Imagery Classifier

Distinguish imagined left-hand vs. right-hand movement from EEG.

## Dataset

- [EEG Motor Movement/Imagery Dataset](https://www.physionet.org/content/eegmmidb/) (PhysioNet)

## Approaches

1. **Classical:** Common Spatial Patterns (CSP) + LDA — strong, interpretable baseline
2. **Deep:** simple CNN on epochs (EEGNet-style) — good contrast in the write-up

## Suggested stack

- MNE, scikit-learn (CSP/LDA), optional PyTorch / Braindecode

## Milestones

1. Load runs for left/right imagery; epoch around cues
2. Filter (e.g. 8–30 Hz); train CSP + LDA
3. Report accuracy / kappa with session-aware CV
4. Compare to a small CNN; plot CSP patterns / topo maps

# Seizure Detection

Flag seizure onset from raw scalp EEG segments (CHB-MIT).

## Dataset

- [CHB-MIT Scalp EEG Database](https://www.physionet.org/content/chbmit/) (PhysioNet)

## Notes

- Highly imbalanced (seizure rare) — emphasize sensitivity and false-positive rate per hour
- Start with one patient, then patient-wise generalization

## Suggested stack

- MNE / WFDB, scikit-learn or PyTorch, strong evaluation hygiene

## Milestones

1. Parse annotations; plot preictal / ictal / interictal windows
2. Features (energy, spectral, line length) or spectrogram CNN
3. Thresholded detector with FPR/h and sensitivity
4. Cross-patient evaluation write-up

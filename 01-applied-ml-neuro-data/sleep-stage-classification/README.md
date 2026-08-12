# Sleep Stage Classification ⭐ starter

Classify sleep stages (Wake / N1 / N2 / N3 / REM) from EEG using Sleep-EDF.

## Why start here

Clean labels, well-documented dataset, and the pipeline (filtering → features → classifier) transfers to motor imagery, seizure detection, and attention models.

## Dataset

- [Sleep-EDF](https://www.physionet.org/content/sleep-edfx/) (PhysioNet)
- Use a small subject subset for v1; expand later

## Suggested stack

- Python, MNE, NumPy, SciPy, scikit-learn
- Optional later: PyTorch 1D CNN / transformer on spectrograms

## Milestones

1. Load one subject, plot raw EEG + hypnogram
2. Bandpass filter; extract bandpower / spectral features per epoch
3. Train Logistic Regression or Random Forest; report per-stage F1
4. Subject-wise CV; confusion matrix figure for portfolio
5. (Stretch) deep model on spectrograms vs. classical baseline

## Layout (once you start coding)

```
notebooks/   # exploration
src/         # reusable pipeline
data/        # local Sleep-EDF (gitignored)
figures/     # portfolio plots
```

# fMRI Cognitive State Decoding

Decode which visual category a subject is looking at from fMRI (Haxby).

## Dataset

- [Haxby et al. 2001](https://nilearn.github.io/stable/modules/generated/nilearn.datasets.fetch_haxby.html) via Nilearn

## Why this one

Small, famous, and purpose-built for a first MVPA / decoding project.

## Suggested stack

- Nilearn, scikit-learn, Matplotlib / Nilearn plotting

## Milestones

1. Load subject data; mask VT / ventral stream ROI
2. Train multiclass decoder (SVM / logistic) on categories
3. Cross-validated accuracy; confusion matrix
4. Searchlight or weight maps for portfolio visuals

# Concepts and metrics primer

No prior statistics background assumed. This is the vocabulary you'll see in every
sleep-staging paper and in this repo's own results tables.

## Signal features

- **Bandpower**: how much signal energy falls in a given frequency range (delta
  0.5–4 Hz, theta 4–8 Hz, alpha 8–13 Hz, sigma/spindle 12–15 Hz, beta 13–30 Hz).
  Sleep stages have characteristic bandpower signatures — e.g. deep sleep (N3) is
  dominated by delta waves, REM looks more like wake in frequency content but has
  distinct eye-movement artifacts in the EOG channel. This is the first feature set
  we'll extract, because it's directly interpretable against what a sleep technician
  would look for on a hypnogram by eye.
- **Spectrogram**: bandpower computed in short sliding windows and stacked over time,
  turning a 1D signal into a 2D time-frequency image. Several deep models (U-Time,
  SleepTransformer) operate on spectrograms rather than raw waveforms.
- **Epoch**: the standard 30-second window that sleep stages are scored on (AASM
  convention). Every model in this plan predicts one label per 30s epoch.
- **Statistical/entropy features** (used by the XGBoost baseline): variance, skewness,
  kurtosis, Higuchi fractal dimension, permutation entropy, spectral edge frequency —
  summary statistics that capture signal complexity/irregularity without assuming a
  specific frequency-domain interpretation.

## Evaluation metrics

- **Accuracy**: percentage of 30-second epochs correctly labeled. Simple, but
  misleading here — a large fraction of any night is N2 sleep, so a model that mostly
  predicts "N2" can score deceptively high accuracy while being useless at detecting
  the rarer stages (N1 especially, which is notoriously hard even for human scorers).
- **Macro F1**: for each stage separately, F1 combines precision ("when the model
  says N1, is it usually right?") and recall ("when N1 actually occurs, does the
  model catch it?") into one number. "Macro" means the five per-stage F1 scores are
  averaged with equal weight, so a model can't hide poor performance on a rare stage
  behind good performance on a common one. This is why papers treat macro F1, not
  accuracy, as the headline number.
- **Cohen's kappa**: how much better the model is than chance agreement, correcting
  for the fact that class imbalance (lots of N2) lets a biased guesser rack up some
  "agreement" with the truth for free. Kappa = 0 means no better than random; 1 means
  perfect agreement. It's also the standard way the field reports human-vs-human
  inter-rater agreement (typically ~0.7–0.8 between two expert scorers on the same
  recording), which gives you a real ceiling to compare model performance against —
  not just "closer to 1 is better" but "closer to human-level agreement is the actual
  goal."

## Subject-wise cross-validation

Never split epochs randomly across train/test — consecutive epochs from the same
night are highly correlated, so a random split leaks information and inflates scores.
Always split by *subject*: all epochs from a given person go entirely into train or
entirely into test. This is standard practice in every paper reviewed for this plan
and is non-negotiable for honest numbers.

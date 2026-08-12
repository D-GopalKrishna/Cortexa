# Focus / Attention Classifier ⭐ starter

Classify focused vs. distracted states from consumer EEG (e.g. Muse). Natural narrative bridge to FocusAnalyze.

## Hardware / data

- Muse headband (or recorded sessions exported offline)
- Start offline on labeled segments; then optional live inference

## Suggested stack

- Muse LSL / brainflow or recorded CSV/EDF
- MNE or SciPy filters; scikit-learn or light deep model
- Bandpower (esp. theta/alpha/beta) as first features

## Milestones

1. Record or load focused vs. distracted sessions; visualize PSD
2. Epoch + bandpower features; train a simple classifier
3. Report accuracy with session-aware CV (no leakage)
4. (Stretch) live stream → state probability meter UI

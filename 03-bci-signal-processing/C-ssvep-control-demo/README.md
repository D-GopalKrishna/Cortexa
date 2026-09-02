# SSVEP-based Control Demo

Flash stimuli at different frequencies; detect which one the user attends to from EEG; map that to a simple control action (cursor, LED, UI highlight).

## Suggested stack

- Stimulus: PsychoPy / Pygame / web CSS animations
- Detection: FFT SNR or CCA on EEG channels
- OpenBCI / Muse via BrainFlow or LSL

## Milestones

1. Offline: known-frequency stimulation; verify spectral peaks
2. Two-class CCA / FFT classifier above chance
3. Closed loop: gaze selection drives a UI state
4. Latency + accuracy write-up for portfolio

# Real-time Blink / Eye-Artifact Detector

Live pipeline that flags eye-blink (and related) artifacts in an EEG stream (OpenBCI or Muse).

## Suggested stack

- BrainFlow / LSL for streaming
- Peak / amplitude / template matching or ICA-inspired heuristics
- Rolling buffer with low latency

## Milestones

1. Offline: detect blinks on recorded EEG; mark events
2. Real-time: stream → window → flag → log / visual indicator
3. Measure false alarms vs. misses on a short labeled session
4. Optional: soft reject / interpolate for downstream BCI use

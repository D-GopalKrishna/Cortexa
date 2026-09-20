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

## Stretch: OpenBCI + C++ bridge + Unity front end

Fold in a compiled real-time path instead of the Python-only loop above.
**No OpenBCI hardware on hand** — so "acquisition" means replaying a recorded
EEG file (e.g. a public SSVEP dataset, or your own offline-phase recording if
you get access to a board later) over LSL at real-time speed, rather than
reading a live board. The rest of the pipeline (bridge, classifier, Unity)
is identical either way, so nothing here is wasted if hardware shows up later.

- **Acquisition**: BrainFlow's playback/synthetic board mode, or a small LSL
  outlet that streams a recorded `.csv`/`.edf` file at the original sample
  rate ([BrainFlow](https://brainflow.org/) has a native C++ API either way)
- **Bridge**: a small C++ process does ring-buffer acquisition, bandpass/notch
  filtering, and FFT-SNR / CCA scoring per stimulus frequency — this is the part
  Python's GIL makes awkward at OpenBCI's native sample rates. Publish the
  per-frequency scores over a local socket or shared memory.
- **Front end**: Unity renders the flickering stimuli (frequency-accurate via
  `Update`/coroutines tied to the render loop) and reads scores from the C++
  bridge to drive a visible action (move a cube, highlight a UI panel) — this
  makes the "stare at the flashing square to move the thing" demo tangible.

Milestones (additive to 1-4 above):

5. Get a recorded/replayed EEG stream into the C++ bridge over LSL; verify the
   same spectral peaks as the offline Python prototype
6. Port the FFT-SNR/CCA classifier from Python to the C++ bridge; match offline
   accuracy
7. Unity scene with real flicker stimuli synced to the bridge's frequency table
8. Closed loop: Unity reads live scores from the bridge and drives object
   control; measure end-to-end latency vs. the Python-only version

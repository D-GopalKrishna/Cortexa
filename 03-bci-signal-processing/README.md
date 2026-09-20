# BCI / Signal Processing

Live and offline pipelines that turn EEG into control signals or state estimates. Signal processing is the core craft here.

## Projects

| # | Project | Hardware / data | Why it matters |
|---|---------|-----------------|----------------|
| A | [Focus / attention classifier](A-focus-attention-classifier/) ⭐ starter | Muse (or recorded EEG) | Product story (FocusAnalyze) |
| B | [Blink / eye-artifact detector](B-blink-artifact-detector/) | OpenBCI or Muse | Real-time cleaning skill |
| C | [SSVEP control demo](C-ssvep-control-demo/) | OpenBCI / Muse + stimulus | Frequency-tagging BCI classic; stretch goal adds a C++ real-time bridge + Unity front end |
| D | [P300 speller](D-p300-speller/) | EEG + matrix stimulus | Attention-based typing demo |
| E | [Neurofeedback in AR/VR](E-neurofeedback-ar-vr/) | OpenBCI + Unity (AR/VR) | Live brain-state score drives an interactive scene — most demoable piece in the track |

## Shared skills to practice

- Streaming buffers, windowing, latency budgets
- Bandpass / notch filters, ICA or template artifact rejection
- CCA / FFT for SSVEP; ERP averaging for P300
- Offline prototype first, then real-time loop
- Information transfer rate (ITR, bits/min) as a decoder metric alongside
  accuracy/F1 — not just D's footnote; report it for A and C's classifiers
  too, since it's the metric that actually reflects "how much of a
  communication channel this gives the user" (theory: [Ch4 of Dayan &
  Abbott](../02-computational-neuroscience/theoretical-neuroscience-book/information-theory/))

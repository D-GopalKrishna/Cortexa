# BCI / Signal Processing

Live and offline pipelines that turn EEG into control signals or state estimates. Signal processing is the core craft here.

## Projects

| # | Project | Hardware / data | Why it matters |
|---|---------|-----------------|----------------|
| A | [Focus / attention classifier](A-focus-attention-classifier/) ⭐ starter | Muse (or recorded EEG) | Product story (FocusAnalyze) |
| B | [Blink / eye-artifact detector](B-blink-artifact-detector/) | OpenBCI or Muse | Real-time cleaning skill |
| C | [SSVEP control demo](C-ssvep-control-demo/) | OpenBCI / Muse + stimulus | Frequency-tagging BCI classic |
| D | [P300 speller](D-p300-speller/) | EEG + matrix stimulus | Attention-based typing demo |

## Shared skills to practice

- Streaming buffers, windowing, latency budgets
- Bandpass / notch filters, ICA or template artifact rejection
- CCA / FFT for SSVEP; ERP averaging for P300
- Offline prototype first, then real-time loop

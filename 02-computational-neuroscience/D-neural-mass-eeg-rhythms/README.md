# Neural Mass Model of EEG Rhythms

Simulate a Wilson–Cowan (or Jansen–Rit) style neural mass model and compare its oscillatory output to real EEG frequency bands.

## Suggested stack

- NumPy / SciPy ODEs, Matplotlib / SciPy signal for spectra
- Optional: compare to a short real EEG snippet (bandpower)

## Milestones

1. Implement Wilson–Cowan E/I equations; find oscillatory parameter regimes
2. Compute power spectrum; label delta–gamma-like peaks
3. Bifurcation / parameter sweep figure
4. Side-by-side with filtered real EEG bands (qualitative compare)

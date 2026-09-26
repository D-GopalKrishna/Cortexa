# In-Vivo Awake-Behaving Decoding

Decode behavior from real spike data recorded in awake, behaving animals —
the closest software-only substitute for the in-vivo electrophysiology and
awake-behaving recordings that
[06-neurostimulation-and-prosthetics](../../06-neurostimulation-and-prosthetics/)
depends on. Everything else in this repo is EEG/fMRI/MEG (surface,
human, low channel count); this project is the first with real single/multi-
unit spikes from an animal performing a task.

## Honest framing

This is real public data, not a simulated stand-in — the spikes, the
behavior, and the noise are all genuine. What it does **not** provide is the
experience of running the session yourself (surgery, headstage, animal
handling, real-time troubleshooting). That gap is named here rather than
glossed over; see the parent track's README for the full caveat.

## Dataset (pick one)

- [IBL Brainwide Map](https://int-brain-lab.github.io/iblenv/) — Neuropixels
  recordings across many brain regions in mice performing a decision task;
  large, well-documented, has an official Python API (`ONE-api`)
- [Allen Institute Visual Coding (Neuropixels)](https://allensdk.readthedocs.io/en/latest/visual_coding_neuropixels.html) —
  visual stimuli + Neuropixels recordings, `AllenSDK` for access
- [DANDI Archive](https://dandiarchive.org/) — browse for a smaller awake-
  behaving session (NWB format) if the above two feel too large for v1

## Suggested stack

- `ONE-api` (IBL) or `AllenSDK`, or `pynwb`/`nwbwidgets` for generic NWB files
- `spikeinterface` if you want to touch raw spike sorting rather than using
  pre-sorted units
- scikit-learn / PyTorch for the decoder itself

## Milestones

1. Load one session; plot raster of a handful of units aligned to a
   behavioral event (e.g. stimulus onset, choice)
2. Basic tuning: which units' firing rates actually vary with the behavioral
   variable of interest (stimulus side, reward, movement)?
3. Population decoder: predict the behavioral variable from simultaneously
   recorded units (start with a simple linear decoder on binned spike counts)
4. Cross-validate across trials; report decoding accuracy vs. chance, and
   vs. number of units used (does accuracy saturate, or keep climbing?)
5. (Stretch) compare decoding accuracy across brain regions if the dataset
   spans several — which region carries the most information about the task?
6. (Stretch) raw spike sorting with `spikeinterface` on one session's raw
   data instead of using pre-sorted units, to see what the "recording" half
   of a recording-and-stimulation experiment actually involves upstream of
   the clean spike trains used above

## Layout

```
notebooks/   # one per phase — exploration, tuning, decoding
src/         # session loading, alignment, decoder
figures/     # rasters, tuning curves, decoding accuracy vs. region/unit-count
```

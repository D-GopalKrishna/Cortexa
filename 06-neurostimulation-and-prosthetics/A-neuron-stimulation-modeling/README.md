# NEURON Stimulation Modeling ⭐ starter

Move from the single-compartment Hodgkin-Huxley model
([02-A](../../02-computational-neuroscience/A-hodgkin-huxley-model/)) to a real
multi-compartment cable model in NEURON, then inject *extracellular*
stimulation (mimicking an implanted electrode) instead of just an intracellular
current step — this is the core of computational models of, and encoding
strategies for, electrical stimulation, and NEURON is the standard tool for
it.

## Why this one first

Everything else in this track depends on being comfortable with NEURON's
model of a neuron as a chain of compartments, and with the distinction between
stimulating a neuron from *inside* (patch electrode, intracellular current —
what 02-A does) vs. from *outside* (extracellular field — what an implant
actually does, and what determines which axons/somas activate first).

## Suggested stack

- [NEURON](https://www.neuron.yale.edu/neuron/) with its Python interface
  (`pip install neuron`)
- [LFPy](https://lfpy.readthedocs.io/) or NEURON's built-in `extracellular`
  mechanism for applying an external field to a compartmental model
- Morphologies: start with NEURON's built-in ball-and-stick, then a real
  reconstructed morphology from [NeuroMorpho.org](https://neuromorpho.org/)

## Milestones

1. Build a ball-and-stick multi-compartment model in NEURON; reproduce a
   propagating action potential along the dendrite (sanity check against
   02-A's single-compartment spike)
2. Apply an extracellular point-source stimulus (the classic McIntyre/Grill
   activating-function approach); find the stimulation amplitude threshold
   that triggers a spike
3. Sweep electrode distance/position; plot threshold vs. distance (strength-
   distance curve) — this is a real quantity implant designers report
4. Load a reconstructed morphology (real axon/dendrite geometry) from
   NeuroMorpho; repeat the threshold analysis and compare to the toy
   ball-and-stick result
5. **Encoding strategy**: design a stimulation *pattern* (e.g. a pulse train
   with varying amplitude/frequency) intended to encode a simple analog value
   (like a light intensity, for the vision-pipeline tie-in in
   [C](../C-prosthetic-vision-pipeline/)), and verify the modeled neuron's
   firing rate actually tracks the encoded value
6. (Stretch) multi-electrode array: model several electrodes with independent
   fields, check for interaction/crosstalk between adjacent electrodes'
   activation zones

## Layout

```
notebooks/   # NEURON model exploration, one per milestone
src/         # reusable model-building + stimulation helper code
figures/     # strength-distance curves, threshold maps, encoding validation
```

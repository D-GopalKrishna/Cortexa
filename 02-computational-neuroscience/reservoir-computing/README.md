# Reservoir Computing / Liquid State Machine

Build a fixed recurrent “reservoir” (or liquid of spiking neurons) and train only the readout for a simple classification or timing task.

## Why it matters

Ties computational neuroscience (dynamics / recurrence) to practical ML (readout learning).

## Suggested stack

- NumPy reservoir, or Brian2 liquid + linear readout
- Optional: Echo State Network (ESN) first, then spiking LSM

## Milestones

1. Implement a small ESN; classify a simple temporal pattern
2. Show that a static feedforward net fails the same temporal task
3. (Stretch) spiking liquid state machine + same readout story
4. Visualize reservoir trajectories / PCA of states

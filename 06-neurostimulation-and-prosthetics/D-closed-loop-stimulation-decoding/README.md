# Closed-Loop Stimulation-Decoding

Wire a decoder and a stimulator into one loop: read simulated neural state,
decide a stimulation pattern, apply it, read the resulting state, repeat.
Every other project in this repo (and tracks A-C in this one) is either
read-only or write-only — this is the only project that closes the loop, the
defining feature of a bidirectional brain-computer interface.

## Prerequisite

Needs [A-neuron-stimulation-modeling](../A-neuron-stimulation-modeling/)
working end-to-end first (a model that responds measurably to a stimulation
pattern) — this project is the control loop wrapped around that model, not a
new simulation from scratch.

## Idea

Pick one concrete closed-loop task rather than a generic loop:

- **Adaptive threshold tracking**: the "patient's" simulated excitability
  drifts over time (mimicking electrode impedance change / tissue response);
  a controller must detect the drift from evoked-response feedback and adjust
  stimulation amplitude to maintain constant activation — this is a real,
  named clinical problem (closed-loop amplitude control) with an
  unambiguous ground truth to evaluate against.
- **Alternative**: closed-loop seizure suppression — detect a seizure-like
  state in [02-B](../../02-computational-neuroscience/B-spiking-neural-network/)'s
  network model (synchrony spike) and trigger a stimulation pulse to
  desynchronize it, then measure suppression latency/success rate.

## Suggested stack

- Reuse A's NEURON model (or 02-B's Brian2 network) as the "plant"
- Python control loop: simple threshold/PID controller first, RL (e.g.
  a small policy learned via stable-baselines3) as a stretch comparison
- Log every loop iteration (state estimate, action taken, outcome) for a
  clear evaluation trace

## Milestones

1. Open-loop baseline: apply a fixed stimulation pattern, show the plant's
   excitability drifting away from target over time (establishes the problem)
2. Closed-loop v1: simple feedback controller (e.g. proportional control on
   evoked-response amplitude) that adjusts stimulation to track a target
3. Quantify: time-to-recovery after an induced disturbance, steady-state
   error, with vs. without closed-loop control
4. Add realistic constraints: measurement noise, feedback delay (real BCI
   loops aren't instantaneous) — show how much delay the controller
   tolerates before it becomes unstable
5. (Stretch) RL-based controller; compare against the hand-tuned feedback
   controller on the same disturbance-recovery benchmark
6. Latency/stability write-up for portfolio — this is the project that best
   demonstrates "designed a closed-loop BCI," so the write-up matters as much
   as the code

## Layout

```
notebooks/   # loop prototyping, one per milestone
src/         # plant (imported from A or 02-B), controller, loop harness
figures/     # disturbance-recovery curves, delay-vs-stability sweep
```

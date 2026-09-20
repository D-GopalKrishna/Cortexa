# Theoretical Neuroscience (Dayan & Abbott)

Study notes/exercises folder for *Theoretical Neuroscience: Computational and
Mathematical Modeling of Neural Systems* (Dayan & Abbott, MIT Press). Companion
in spirit to [Sterratt et al., *Principles of Computational Modelling in
Neuroscience*](../A-hodgkin-huxley-model/) (the book behind 02-A) but a
different question: where Sterratt asks "how do you simulate a neuron/circuit
mechanistically," Dayan & Abbott asks "how do you treat neural activity as a
**code** — what does a spike train represent, and how do you measure that
rigorously." One folder per in-scope chapter.

## Chapters

| # | Chapter | Folder | In scope? |
|---|---------|--------|-----------|
| 1 | Neural encoding I — firing rates, spike statistics | [neural-encoding-firing-rates/](neural-encoding-firing-rates/) | Yes |
| 2 | Neural encoding II — reverse correlation, receptive fields | [neural-encoding-receptive-fields/](neural-encoding-receptive-fields/) | Yes |
| 3 | Neural decoding | [neural-decoding/](neural-decoding/) | Yes |
| 4 | Information theory | [information-theory/](information-theory/) | Yes |
| 5 | Model neurons I — neuroelectronics | [model-neurons-neuroelectronics/](model-neurons-neuroelectronics/) | Yes |
| 6 | Model neurons II — conductances, morphology | [model-neurons-conductances-morphology/](model-neurons-conductances-morphology/) | Yes |
| 7 | Network models | [network-models/](network-models/) | Yes |
| 8 | Plasticity and learning | [plasticity-and-learning/](plasticity-and-learning/) | Yes |
| 9 | Classical conditioning and reinforcement learning | — | No |
| 10 | Representational learning | — | No |

Chapters 9-10 are animal-behavior/RL-theory territory with little direct
line to this portfolio's BCI/connectomics/neurostimulation focus — left out
deliberately rather than built and left unused. Revisit if a future project
actually needs them (e.g. RL shows up if a closed-loop stimulation project
wants a policy-learning framing).

## Why this lives here, not as a lettered project (A/B/C...)

This is book study, not a project — no single deliverable, no milestones
list. Each chapter folder holds whatever notebook/notes make the chapter's
concepts concrete, and gets referenced from the actual project READMEs
(02-A, and track 03's BCI decoders) where the ideas apply, rather than
duplicating them there.

## Where the ideas actually land in the repo

- **Ch1-3 (encoding/decoding)** — this is what every classifier in
  [03-bci-signal-processing](../../03-bci-signal-processing/) already does in
  practice; these chapters are the theory under that track's practice.
- **Ch4 (information theory)** — promoted to a named shared skill in
  [03's README](../../03-bci-signal-processing/README.md) (ITR / mutual
  information as a decoder metric, not just a 03-D footnote).
- **Ch5-6 (model neurons)** — same territory as 02-A (single neuron) and its
  Part 2 compartmental/propagation extension.
- **Ch7 (network models)** — overlaps 02-B (spiking network) and 02-C
  (reservoir computing).
- **Ch8 (plasticity/learning)** — currently a gap; would matter most for
  02-B if it moves from a fixed-weight network to a biologically plausible
  learning rule (e.g. STDP) instead of backprop.

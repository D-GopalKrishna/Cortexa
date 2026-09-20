# Neurostimulation & Prosthetics

## ⚠️ Scope note: this track is derived from a Neuralink job posting

This track exists to close a specific, named gap: the "Neuroengineer, Next Gen"
role at Neuralink requires computational modeling of electrical stimulation
(NEURON, FEM electric fields), a prosthetic vision pipeline (machine vision +
smart glasses + eye tracking), and closed-loop bidirectional BCI — none of
which the rest of this portfolio (all read-only: EEG/fMRI/MEG → classify)
touches. The track's scope, project boundaries, and vocabulary below are
shaped directly by that job description, not by a general survey of the
stimulation/prosthetics literature. Treat it as "build fluency against a real
industry bar," not as original research scoping.

The role also requires in-vivo electrophysiology, awake behaving recordings,
and hands-on instrumentation — those are **not** solvable by solo software
projects and are called out as an honest gap rather than faked here. See
[01-applied-ml-neuro-data/G-invivo-awake-behaving-decoding](../01-applied-ml-neuro-data/G-invivo-awake-behaving-decoding/)
for the closest software-only substitute (real public spike data, not a lab
session).

## Why this track is different from the rest of the portfolio

Every other track in this repo *reads* brain signals (decode EEG/fMRI/MEG into
a label). This track *writes* to the brain (model what stimulation does to
neural tissue) and eventually *closes the loop* (read + write together) — a
different half of the BCI problem entirely.

## Projects

| # | Project | Core skill | JD bullet it targets |
|---|---------|-----------|----------------------|
| A | [NEURON stimulation modeling](A-neuron-stimulation-modeling/) ⭐ starter | Multi-compartment cable modeling, extracellular stimulation | "Computational models of ... electrical stimulation"; "NEURON modeling environment" |
| B | [FEM electric field modeling](B-fem-electric-field-modeling/) | Volume-conductor / finite element modeling of current spread | "Modeling electric fields using finite element modeling (FEM)" |
| C | [Prosthetic vision pipeline](C-prosthetic-vision-pipeline/) | Machine vision, phosphene simulation, eye tracking | "End-to-end hardware and software solutions for prosthetic vision ... machine vision algorithms, smart glasses, and eye tracking" |
| D | [Closed-loop stimulation-decoding](D-closed-loop-stimulation-decoding/) | Bidirectional BCI loop | "Closed-loop brain-computer interface" |

## Suggested order

A → B (B's field output becomes A's stimulation input) → C (independent,
can run in parallel) → D (needs A working end-to-end first).

## Background study (watch before/alongside A-D)

[NPTEL Neural Science for Engineers](https://www.youtube.com/playlist?list=PLgMDNELGJ1CZ_lZXJH0IzTR5SD5nL_-5m)
+ its follow-up [Advanced Neural Science for Engineers](https://archive.nptel.ac.in/content/syllabus_pdf/108108188.pdf)
(both free, Prof. Vikas V, NIMHANS Neurosurgery) map onto this track almost
1:1: BCI device design and biopotential acquisition (base course) then
microelectrode array fabrication, invasive recording, deep brain stimulation,
and COMSOL-based FEM simulation for neural engineering (advanced course) —
the advanced course's Week 10 is literally B's FEM project using the
industry-standard tool. Watch base → advanced, in parallel with A-D.

## Honest limits

No hardware, no animals, no wet lab. Every project here is a simulation or a
software-only pipeline. That gets you to "can model, reason about, and speak
fluently about stimulation and closed-loop BCI" — it does not substitute for
actual in-vivo experience, which the JD explicitly lists as required/preferred.

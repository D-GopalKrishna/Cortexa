# Plan overview

This project walks through the actual historical/technical evolution of automated
sleep stage classification — classical features → deep learning → attention/transformer
→ efficient deployment → foundation models — using it as a teaching arc as much as an
implementation one. Each phase produces a working, evaluated model before moving on, so
the portfolio ends up with a genuine comparison table, not just a final black box.

## Reading order

1. [01-concepts-and-metrics.md](01-concepts-and-metrics.md) — plain-language primer on
   accuracy / macro F1 / Cohen's kappa, and the signal-processing vocabulary (bandpower,
   spectrograms) used throughout. Read this first if the stats terms in the original
   README felt unfamiliar.
2. [02-datasets.md](02-datasets.md) — every dataset we'll touch, what it's good for, and
   where to get it.
3. [03-model-landscape.md](03-model-landscape.md) — the architecture evolution, verified
   against the literature, with corrections to a couple of names/years that came in
   slightly garbled.
4. [04-phases.md](04-phases.md) — the actual phase-by-phase build plan, mapped to
   folders/notebooks/scripts in this repo.

## Why this order (classical → deep → attention → efficient → foundation)

- **Classical first** because it's fast to iterate, forces you to understand the signal
  (bandpower, spectral features) before trusting a model to learn it, and gives every
  later model a baseline to beat.
- **Deep learning next** (DeepSleepNet-style CNN+LSTM) because it's the historical
  starting point of the field (2017) and the simplest "raw signal in, stage out"
  architecture.
- **Sequence and attention models** (SeqSleepNet, AttnSleep, SleepTransformer) because
  sleep staging is fundamentally sequential — a single 30s epoch is often ambiguous
  without the surrounding context, and this is where most of the field's accuracy gains
  actually came from.
- **Efficiency/deployment** (TinySleepNet) as a deliberate detour: once you have an
  accurate model, ask what it costs to run on a wearable, and what accuracy you give up
  to get there. This is a genuinely different optimization target and worth its own
  phase rather than an afterthought.
- **Foundation models** last, because fine-tuning a pretrained EEG encoder (EEGPT,
  BIOT, LaBraM, CBraMod) only means something once you have your own from-scratch
  numbers to compare it against — otherwise you can't tell if the pretraining actually
  helped.

## Guiding constraint

Every phase reports the same three metrics (accuracy, macro F1, Cohen's kappa) on the
same held-out subject-wise split, so results are comparable across the whole arc. See
[results/](../results/) for the running comparison table once phases start producing
numbers.

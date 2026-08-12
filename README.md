# Neurotechnology Portfolio

Four tracks for studying and shipping portfolio-ready neurotech projects. Each folder is a self-contained subproject with its own study notes and build path.

## Tracks

| # | Track | Starter project |
|---|--------|-----------------|
| 01 | [Applied ML on Neuro Data](01-applied-ml-neuro-data/) | Sleep stage classification |
| 02 | [Computational Neuroscience](02-computational-neuroscience/) | Hodgkin–Huxley model |
| 03 | [BCI / Signal Processing](03-bci-signal-processing/) | Focus / attention classifier |
| 04 | [Connectomics](04-connectomics/) | Graph-theoretic analysis (C. elegans) or Tracing QA |

## Suggested study order

1. **Sleep stage classification** — clean labels, classic EEG pipeline (filter → features → classifier).
2. **Hodgkin–Huxley** — equations-level single-neuron intuition.
3. **Focus / attention classifier** — consumer EEG + product narrative (FocusAnalyze).
4. **Tracing QA tool** — connectomics + NeuroGlass-relevant tooling.

Then branch into the remaining projects in each track as you deepen the portfolio.

## Conventions

- Each project folder has a `README.md` (goal, dataset, stack, milestones).
- Put notebooks in `notebooks/`, scripts in `src/`, figures in `figures/`, and local data under `data/` (gitignored when you init repos).
- Prefer small, demable v1s over large unfinished systems.

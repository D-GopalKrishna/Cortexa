# Neurotechnology Portfolio

Seven tracks for studying and exploring neurotech, one buildable project at a time. Each folder is a self-contained subproject with its own study notes and build path.

No BCI hardware (OpenBCI, Muse, etc.) is available — projects that would
normally use live acquisition are scoped to run on recorded/public datasets
instead (see the hardware note in each affected project's README).

Tracks 06 and 07 are deliberately narrow: each was scoped around a specific
set of applied skills (06: stimulation and prosthetics modeling; 07: clinical
and health data engineering) rather than as a general survey of the field —
see each README's scope note.

## Tracks

| # | Track | Starter project |
|---|--------|-----------------|
| 01 | [Applied ML on Neuro Data](01-applied-ml-neuro-data/) | Sleep stage classification |
| 02 | [Computational Neuroscience](02-computational-neuroscience/) | Hodgkin–Huxley model |
| 03 | [BCI / Signal Processing](03-bci-signal-processing/) | Focus / attention classifier |
| 04 | [Connectomics](04-connectomics/) | Graph-theoretic analysis (C. elegans) or Tracing QA |
| 05 | [Multimodal Biosensing](05-multimodal-biosensing/) | Multimodal emotion/state fusion (Galea-style) |
| 06 | [Neurostimulation & Prosthetics](06-neurostimulation-and-prosthetics/) ⚠️ narrowly scoped (see track README) | NEURON stimulation modeling |
| 07 | [Clinical / Health Data Engineering](07-clinical-health-data-engineering/) ⚠️ narrowly scoped (see track README) | Healthcare data standards interop (EDF → FHIR) |

## Suggested study order

1. **01-A Sleep stage classification** — clean labels, classic EEG pipeline (filter → features → classifier).
2. **02-A Hodgkin–Huxley** — equations-level single-neuron intuition.
3. **03-A Focus / attention classifier** — consumer EEG + product narrative (FocusAnalyze).
4. **04-B Tracing QA tool** — connectomics + NeuroGlass-relevant tooling (or **04-A** for a faster graph win).

Then continue with B / C / D (and E for MEG) in each track as you go deeper.

## Conventions

- Tracks are numbered `01`–`04`; projects inside each track use letter prefixes `A`–`E` (starter = `A` where marked).
- Each project folder has a `README.md` (goal, dataset, stack, milestones).
- Put notebooks in `notebooks/`, scripts in `src/`, figures in `figures/`, and local data under `data/` (gitignored when you init repos).
- Prefer small, demable v1s over large unfinished systems.

# Neurotech portfolio — repo instructions

## Obsidian study notes

Study notes for this repo live outside the repo, in Obsidian, at:

```
/Users/dgk.mac/Library/CloudStorage/GoogleDrive-nikhil0223@gmail.com/My Drive/Studies/Neuroscience/Mini Neurotech projects notes
```

Mirrors the repo's track/project numbering (e.g. `01-sleep-stage-classification/`
corresponds to `01-applied-ml-neuro-data/A-sleep-stage-classification/`).

**Only write there when explicitly asked to** — don't proactively sync chat content
into Obsidian notes as a side effect of other work.

**Never overwrite the user's own writing.** These notes are a mix of the user's own
notes and anything Claude adds — never assume a file (or section) is safe to
regenerate wholesale. Before editing an existing note, read the whole file first.

**Tag every addition as AI-written.** Anything Claude writes or edits into these
notes — a new section, a new file, an edit to an existing line — must be clearly
marked so it's distinguishable from the user's own writing at a glance. Prefix
AI-added sections with an `> [!ai] AI notes` callout (Obsidian callout syntax) or,
for smaller inline additions, an `*(AI)*` tag. Never blend AI-written content into
a paragraph the user wrote without a visible boundary.

## Python environment

Use the shared conda env `neurofolio` (`/Users/dgk.mac/miniconda3/envs/neurofolio`) for
notebooks and scripts across this repo, instead of creating a new per-project `.venv`.
Activate with `source /Users/dgk.mac/miniconda3/bin/activate neurofolio`. If a project
needs a package the env doesn't have, `pip install` it into `neurofolio` rather than
spinning up an isolated venv. Some older projects (e.g.
`01-applied-ml-neuro-data/A-sleep-stage-classification`,
`02-computational-neuroscience/A-hodgkin-huxley-model`) already have their own
`.venv` — leave those as-is, this only applies going forward.

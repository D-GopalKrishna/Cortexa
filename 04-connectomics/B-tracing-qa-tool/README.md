# Tracing QA Tool

Flag likely annotation errors in a traced dataset — disconnected segments, orphan nodes, degree outliers. Directly inspired by NeuroGlass-style pain points.

## Data

- Synthetic broken traces first (controlled errors)
- Then a public partial connectome or export from a tracing tool

## Suggested stack

- NetworkX / custom graph from skeleton segments
- Rules + optional light ML on local features
- Report UI: table of flags + link to node IDs

## Milestones

1. Define error types; generate synthetic positives
2. Detectors: orphans, disconnects, stubby dead-ends, impossible degrees
3. Precision/recall on synthetic set
4. Run on a real export; case-study screenshots for portfolio

# Connectome Comparison Viewer

Visualize and diff two versions of a traced circuit (annotator agreement / revision QA).

## Use cases

- Two annotators on the same volume
- Before/after proofreading passes
- Echoes real NeuroGlass workflow friction

## Suggested stack

- Graph isomorphism-lite diffs: shared nodes/edges, unique to A/B
- Overlay viz (color by agreement)
- Optional: edge-weight / synapse-count deltas

## Milestones

1. Load two edge lists with shared ID space (or mapping)
2. Compute intersection / symmetric difference stats
3. Side-by-side or overlay visualization
4. Export a disagreement report

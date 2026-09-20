# Connectomics

Graph tools and QA over traced circuits — natural extension of NeuroGlass-style annotation work.

## Projects

| # | Project | Data | Why it matters |
|---|---------|------|----------------|
| A | [Graph-theoretic analysis](A-graph-theoretic-analysis/) | C. elegans (or similar) | Small, fully mapped; fast results |
| B | [Tracing QA tool](B-tracing-qa-tool/) | Synthetic or public traces | Direct NeuroGlass narrative |
| C | [FlyWire circuit explorer](C-flywire-circuit-explorer/) | FlyWire subset | Query / hop exploration at scale |
| D | [Connectome comparison viewer](D-connectome-comparison-viewer/) | Two versions of a circuit | Annotator agreement / QA diffs |
| E | [Connectomics data pipeline & compression engineering](E-connectomics-data-pipeline-engineering/) | EM volumes / segmentation / mesh chunks | Extends real prior Virtual Fly Brain pipeline/compression work — the track's demonstrated strength, not a new skill |

## Shared skills to practice

- NetworkX / graph-tool basics
- Centrality, modularity, motifs, path queries
- Visualization of large sparse graphs
- Error heuristics: orphans, disconnects, degree outliers
- Data pipeline engineering: chunked storage formats, compression trade-offs, throughput at scale (E)

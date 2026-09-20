# FlyWire Circuit Explorer

Pull a subset of the FlyWire connectome and build a graph tool to explore / query circuits (e.g. neurons within two hops of a seed).

## Data

- [FlyWire](https://flywire.ai/) / Codex / public releases — start with a small neighborhood dump, not the full brain

## Related — prior real experience

- [Virtual Fly Brain](https://www.virtualflybrain.org/) — free, public anatomical/ontology
  reference layer that cross-registers FlyWire and hemibrain data onto standard brain
  templates (neuron identity, standard location, cross-paper naming). Complements this
  project's raw wiring-graph queries rather than duplicating them — has a Python client
  (`vfb_connect`, github.com/VirtualFlyBrain) worth using once a subgraph is queryable
  here, to resolve what a queried neuron actually is.
- Already have real pipeline experience here, not just familiarity: prior contribution
  to VFB's data pipeline scripts, specifically improving storage compression. See
  [E-connectomics-data-pipeline-engineering](../E-connectomics-data-pipeline-engineering/)
  for the project that extends that real work into a benchmarked, documented portfolio
  piece — worth doing alongside or before this one, since it's the track's actual
  demonstrated strength rather than a new skill being learned from scratch.

## Suggested stack

- Python, NetworkX or graph-tool, optional Neo4j for queries
- Streamlit / Jupyter for exploration UI

## Milestones

1. Ingest a local edge list subset into a graph
2. Queries: k-hop neighborhood, common partners, path between A–B
3. Simple interactive viz of a queried subgraph
4. Document one biological circuit story you found

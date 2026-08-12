# FlyWire Circuit Explorer

Pull a subset of the FlyWire connectome and build a graph tool to explore / query circuits (e.g. neurons within two hops of a seed).

## Data

- [FlyWire](https://flywire.ai/) / Codex / public releases — start with a small neighborhood dump, not the full brain

## Suggested stack

- Python, NetworkX or graph-tool, optional Neo4j for queries
- Streamlit / Jupyter for exploration UI

## Milestones

1. Ingest a local edge list subset into a graph
2. Queries: k-hop neighborhood, common partners, path between A–B
3. Simple interactive viz of a queried subgraph
4. Document one biological circuit story you found

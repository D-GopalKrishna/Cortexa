# Graph-Theoretic Analysis of a Public Connectome

Compute centrality, modularity, and related metrics on a fully mapped small connectome (e.g. *C. elegans*) and visualize findings.

## Why a good early connectomics project

Tiny, complete, and public — you get real graph science results without FlyWire-scale data engineering.

## Data

- *C. elegans* hermaphrodite connectome (e.g. WormWiring / published adjacency lists)

## Suggested stack

- NetworkX, community detection (Louvain), Matplotlib / Plotly

## Milestones

1. Load directed/weighted synapse graph
2. Degree, betweenness, PageRank; identify hubs
3. Community structure; plot modularity
4. Short write-up: what the metrics suggest biologically

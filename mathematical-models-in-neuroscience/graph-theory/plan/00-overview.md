# Plan overview

This is a study/practice track, not a portfolio deliverable — goal is to build
real intuition for network metrics before applying them to the connectome
project ([04-connectomics/A-graph-theoretic-analysis](../../../04-connectomics/A-graph-theoretic-analysis/)).
One notebook, worked through in order on small toy graphs, each concept
checked against a known/expected result before moving on.

## Toy graphs used throughout

- Zachary's Karate Club (`nx.karate_club_graph()`) — real small social network,
  has known ground-truth community split
- Erdős–Rényi random graph `G(n, p)` — baseline "no structure" null model
- Watts–Strogatz small-world graph — tunable rewiring probability, the
  canonical small-world demo
- (Optional) Barabási–Albert graph — preferential attachment, canonical
  scale-free demo, useful contrast against WS

## Part 1 — degree, clustering, path length

1. Degree distribution (histogram) for each toy graph.
2. Local clustering coefficient per node + global transitivity. Sanity check:
   complete graph → 1.0, tree → 0.0.
3. Average shortest path length and diameter. Sanity check on a small graph
   by hand-counting a couple of paths.
4. Put C (clustering) and L (path length) side by side across ER, WS (varying
   rewiring probability), and BA — this is the setup for the small-world
   comparison in Part 3.

## Part 2 — centrality family

1. Degree centrality, betweenness centrality, closeness centrality,
   eigenvector centrality, PageRank — compute all five on Karate Club.
2. Rank nodes by each measure and compare rankings — the point is seeing
   *where they disagree* (e.g. a high-degree node that isn't a betweenness
   bottleneck, or vice versa), not just computing numbers.
3. Visualize: draw the graph with node size/color mapped to one centrality
   measure at a time.

## Part 3 — small-world and scale-free properties

1. Small-world-ness: compute C and L for the WS graph across a sweep of
   rewiring probability p (0 → mostly regular lattice, 1 → mostly random),
   reproduce the qualitative Watts-Strogatz result (high C, low L in the
   middle range). Compare against `nx.smallworld.sigma` /
   `nx.smallworld.omega` if runtime allows (both are expensive — subsample or
   cap graph size).
2. Degree distribution shape: plot ER vs. BA degree distributions on
   log-log axes — BA should show the heavy tail / approximate power law, ER
   should look Poisson/binomial. This is the practice rep for the scale-free
   check we'll run on the real connectome next.

## Part 4 — community detection

1. Louvain community detection (`python-louvain` / `nx.community.louvain_communities`)
   on Karate Club.
2. Compare detected communities against the known real-world split (the
   club's actual 1977 fission into two factions) — this is the ground-truth
   check that makes Karate Club worth using over a purely synthetic graph.
3. Report modularity score for the detected partition.

## Guiding constraint

Every metric gets a sanity check before moving on — either against a known
closed-form value (complete graph clustering = 1), a documented property of a
named graph (Karate Club's real faction split), or a qualitative textbook
result (Watts-Strogatz C/L curve shape). The point of this track is verified
intuition, not just "a number came out" — same constraint as
[02-A's HH plan](../../../02-computational-neuroscience/A-hodgkin-huxley-model/plan/00-overview.md).

## Next

Once Parts 1–4 are solid, move to the real project: load the C. elegans
connectome and run the same metric families on real synaptic data, checking
findings against known biology (e.g. AVA/AVB as hub interneurons). That work
lives in
[04-connectomics/A-graph-theoretic-analysis](../../../04-connectomics/A-graph-theoretic-analysis/),
not here.

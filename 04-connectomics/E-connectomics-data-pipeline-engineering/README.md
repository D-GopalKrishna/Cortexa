# Connectomics Data Pipeline & Compression Engineering

Extend real prior work — improving storage compression in Virtual Fly Brain's
data pipeline scripts — into a benchmarked, documented portfolio project.
Unlike every other project in this track (which start from "learn the
domain"), this one starts from actual demonstrated experience: building data
pipelines and reducing storage footprint via compression is a real skill
already exercised on a real, public connectomics infrastructure project.

## Why this is different from C/D

C (FlyWire circuit explorer) and D (connectome comparison viewer) are graph-
query and visualization skills, learned fresh. This project is data
*engineering* — ingestion, storage format, compression trade-offs — which is
exactly the skill large connectomics datasets bottleneck on: EM volumes and
their derived segmentations/meshes are terabytes-to-petabytes, and pipeline
storage/compression choices directly determine what's even queryable at
interactive speed (relevant to C's "query a subgraph" experience too).

## Why it also matters for the stimulation track

[06-neurostimulation-and-prosthetics](../../06-neurostimulation-and-prosthetics/)
sits next to high-dimensional neural recording at scale — the same
storage/throughput pipeline problem, just electrophysiology instead of EM
volumes. This project is the one place in the repo that explores the
data-engineering half of that problem directly, rather than only the modeling
half.

## Idea

1. Get a concrete before/after: pull a real (or realistically-sized) chunk of
   connectomics data — an EM image volume, a segmentation mask volume, or a
   skeleton/mesh export — in whatever raw format it's typically distributed in
2. Benchmark multiple compression approaches against it: general-purpose
   (zstd, lz4, gzip) vs. domain-specific (JPEG2000 or PNG for EM image
   volumes, mesh-specific compression like Draco for segmentation meshes)
3. Measure the actual trade-off space: compression ratio vs. compress/decompress
   speed vs. random-access-ability (can you still cheaply read one chunk
   without decompressing the whole volume? — this is the constraint that
   usually matters more than raw ratio for a query pipeline like C's)
4. If possible, write up the *specific* compression change you already made in
   VFB's pipeline as a case study — what format, what algorithm, what the
   measured storage reduction was, what it cost in read latency

## Suggested stack

- Chunked array storage: [Zarr](https://zarr.readthedocs.io/) or
  [N5](https://github.com/saalfeldlab/n5) — the formats real EM/connectomics
  pipelines (CATMAID, FlyWire, Neuroglancer-backed stacks) actually use,
  precisely because they support chunk-level random access under compression
- Compression codecs via [numcodecs](https://numcodecs.readthedocs.io/)
  (blosc/zstd/lz4) plus format-specific options (JPEG2000 via `glymur` or
  `imagecodecs`, Draco for meshes)
- `dask` if the benchmark data is large enough to need out-of-core processing

## Milestones

1. Get one representative chunk of connectomics-style data (image volume,
   segmentation, or mesh) into a local benchmark harness
2. Benchmark ratio + speed for 3-4 compression codecs; table + plot
3. Benchmark chunk size's effect on random-access read latency under each
   codec — the real pipeline-design decision, not just "which codec wins"
4. Case study write-up of the actual VFB pipeline improvement: what was
   changed, measured storage reduction, any latency trade-off observed
5. (Stretch) propose and prototype one further compression/format
   improvement to the same or a similar pipeline, with a measured result

## Layout

```
notebooks/   # benchmark harness, one per compression comparison
data/        # local benchmark chunks (gitignored)
figures/     # ratio-vs-speed, chunk-size-vs-latency plots
results/     # benchmark tables, VFB case study writeup
```

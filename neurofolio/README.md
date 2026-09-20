# Neurofolio

The top-level navigation hub for this portfolio — one static page listing all 4
tracks and their projects, with a link out to each track's own showcase server as
it comes online (track 01's is live now at [../01-applied-ml-neuro-data/showcase](../01-applied-ml-neuro-data/showcase/)).

Deliberately just navigation, not a proxy or a bigger combined server: each
track's showcase already owns its own backend/frontend, and this page just points
at them. If a track ever needs its own showcase server, that's a `showcase/`
folder inside that track (matching track 01's pattern), and `tracks.json` here
gets a `showcaseUrl` update — no changes to how this hub works.

## Run it

```bash
cd neurofolio
python3 serve.py        # http://127.0.0.1:8600
```

No build step, no dependencies — plain HTML/CSS/JS served by Python's stdlib
`http.server`. Track/project metadata lives in `tracks.json`; edit that file to
add projects or flip a status (`planned` / `in_progress` / `done`).

## Files

- `index.html` — the page (fetches `tracks.json`, renders track sections)
- `tracks.json` — data: track number/title/showcase URL + each project's id/title/status
- `serve.py` — tiny stdlib static server (default port 8600)

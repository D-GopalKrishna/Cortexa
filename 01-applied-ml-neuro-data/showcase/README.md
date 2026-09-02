# Showcase

A small dashboard for the 5 [applied-ml-neuro-data](../) projects — one tab per
project (A–E), pulling metadata from a Flask API and (as each project's Phase 11
"Serving & the showcase app" lands) running its actual model against a held-out
sample.

- `frontend/` — Vite + React + TypeScript + Tailwind + shadcn/ui (`radix-nova`
  preset). Tabs list the 5 projects; each tab is a card with the project's dataset,
  blurb, status badge, and a "Run demo" button.
- `backend/` — a small Flask app serving project metadata and a per-project
  `/predict` endpoint. Right now `/predict` returns a clear "not implemented yet"
  response for every project — it's a real, working stub, not a mock, so wiring in
  an actual model later (per each project's own phase plan) is a drop-in change to
  `app.py`, not a rewrite.

## Run it

Two terminals:

```bash
# backend
cd showcase/backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py          # http://127.0.0.1:5050

# frontend
cd showcase/frontend
npm install
npm run dev             # http://localhost:5173
```

The Vite dev server proxies `/api/*` to `http://127.0.0.1:5050` (see
`vite.config.ts`), so the frontend never hardcodes the backend's port.

## Wiring a real model into a project's tab

Each project's `plan/04-phases.md` (see
[A-sleep-stage-classification](../A-sleep-stage-classification/plan/04-phases.md)
Phase 11 for the pattern) ends with a serving phase that exports a small
`src/eval/predict.py`-style function. To surface it here:

1. Import that function in `backend/app.py`'s `project_predict` route, keyed by
   `project_id`.
2. Replace the 501 stub for that one project with a real call — everything else
   (metadata, tabs, status badges) keeps working unchanged.
3. Bump that project's `status` in `backend/projects.py` from `planned`/`in_progress`
   to `done` once it has a working demo.

No project needs to wait for the others — wire each one in as soon as its own phase
plan produces a working model, rather than treating this as one big integration at
the end.

## Extending the frontend

New shadcn components: `npx shadcn@latest add <component>` from `frontend/`. The
project uses the `radix-nova` preset (Lucide icons, Geist font) — keep new
components consistent with that rather than mixing presets.

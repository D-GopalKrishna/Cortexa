"""Static metadata for the 5 applied-ml-neuro-data projects shown in the showcase.

Kept as plain data (not parsed from READMEs) so the API has one obvious source of
truth; update this alongside the top-level 01-applied-ml-neuro-data/README.md table
when a project's status or blurb changes.
"""

PROJECTS = [
    {
        "id": "A",
        "slug": "A-sleep-stage-classification",
        "title": "Sleep stage classification",
        "dataset": "Sleep-EDF",
        "blurb": "Classify Wake/N1/N2/N3/REM from EEG. Cleanest labels; the pipeline this project builds reuses everywhere else in this repo.",
        "status": "in_progress",
        "starter": True,
    },
    {
        "id": "B",
        "slug": "B-motor-imagery-classifier",
        "title": "Motor imagery classifier",
        "dataset": "PhysioNet EEG Motor Movement/Imagery",
        "blurb": "Classic BCI ML baseline (CSP+LDA or CNN) on motor imagery EEG.",
        "status": "planned",
        "starter": False,
    },
    {
        "id": "C",
        "slug": "C-seizure-detection",
        "title": "Seizure detection",
        "dataset": "CHB-MIT Scalp EEG",
        "blurb": "Clinically motivated — detecting seizure onset from scalp EEG.",
        "status": "planned",
        "starter": False,
    },
    {
        "id": "D",
        "slug": "D-fmri-cognitive-state-decoding",
        "title": "fMRI cognitive state decoding",
        "dataset": "Haxby",
        "blurb": "First fMRI project in the repo; famous, small, well-documented dataset.",
        "status": "planned",
        "starter": False,
    },
    {
        "id": "E",
        "slug": "E-meg-preprocessing-information-retrieval",
        "title": "MEG preprocessing & information retrieval",
        "dataset": "MNE sample / OpenNeuro MEG",
        "blurb": "Sensor cleaning pipeline through to evoked responses / decoding.",
        "status": "planned",
        "starter": False,
    },
]


def get_project(slug_or_id: str):
    for p in PROJECTS:
        if p["slug"] == slug_or_id or p["id"] == slug_or_id:
            return p
    return None

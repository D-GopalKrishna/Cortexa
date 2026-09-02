"""Download a subset of Sleep-EDF's "Sleep Cassette" recordings into data/raw/.

Deliberately Sleep Cassette only (not Sleep Telemetry) and a small subject
subset by default — see plan/02-datasets.md for why. Re-runnable: the local
data/raw/ dump is gitignored and expected to be deleted between sessions, so
this script is the reproducible way back to it, not a one-off.

Default source is PhysioNet's official S3 mirror (public, unsigned requests,
no AWS account needed) via the `aws` CLI — this is ~100x faster in practice
than MNE's built-in fetcher, which pulls one file at a time over plain HTTPS
from PhysioNet's own server. The MNE fetcher is kept as a --source physionet
fallback for machines without the `aws` CLI installed.

Usage:
    python -m server.data.download                  # 10 subjects, both nights, via S3
    python -m server.data.download --n-subjects 20
    python -m server.data.download --subjects 0 1 2 --recordings 1
    python -m server.data.download --source physionet  # slow fallback, no aws CLI needed
"""

import argparse
import shutil
import subprocess
from pathlib import Path

# Subjects 39, 68, 69, 78, 79 have no Sleep Cassette recording (per MNE docs).
MISSING_SUBJECTS = {39, 68, 69, 78, 79}
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA_DIR = PROJECT_ROOT / "data" / "raw"
S3_BUCKET_PREFIX = "s3://physionet-open/sleep-edfx/1.0.0/sleep-cassette"


def default_subjects(n: int) -> list[int]:
    available = [s for s in range(83) if s not in MISSING_SUBJECTS]
    return available[:n]


def download_via_s3(subjects: list[int], recordings: list[int], data_dir: Path) -> list[Path]:
    if shutil.which("aws") is None:
        raise RuntimeError(
            "aws CLI not found on PATH. Install it, or re-run with --source physionet."
        )
    out_dir = data_dir / "physionet-sleep-data"
    out_dir.mkdir(parents=True, exist_ok=True)
    downloaded = []
    for s in subjects:
        for night in recordings:
            prefix = f"SC4{s:02d}{night}"
            listing = subprocess.run(
                ["aws", "s3", "ls", "--no-sign-request", f"{S3_BUCKET_PREFIX}/{prefix}"],
                capture_output=True,
                text=True,
                check=False,
            )
            if listing.returncode != 0 or not listing.stdout.strip():
                print(f"  (no recording {night} for subject {s}, skipping)")
                continue
            filenames = [line.split()[-1] for line in listing.stdout.splitlines() if line.strip()]
            for filename in filenames:
                dest = out_dir / filename
                if dest.exists():
                    downloaded.append(dest)
                    continue
                subprocess.run(
                    [
                        "aws", "s3", "cp", "--no-sign-request", "--quiet",
                        f"{S3_BUCKET_PREFIX}/{filename}", str(dest),
                    ],
                    check=True,
                )
                downloaded.append(dest)
    return downloaded


def download_via_physionet(subjects: list[int], recordings: list[int], data_dir: Path) -> list[Path]:
    from mne.datasets.sleep_physionet.age import fetch_data

    data_dir.mkdir(parents=True, exist_ok=True)
    paths = fetch_data(subjects=subjects, recording=recordings, path=str(data_dir))
    return [Path(p) for pair in paths for p in pair]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--n-subjects", type=int, default=10)
    parser.add_argument("--subjects", type=int, nargs="+", default=None)
    parser.add_argument("--recordings", type=int, nargs="+", default=[1, 2], choices=[1, 2])
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument(
        "--source", choices=["s3", "physionet"], default="s3",
        help="s3 (fast, needs aws CLI, default) or physionet (slow, needs only mne).",
    )
    args = parser.parse_args()

    subjects = args.subjects if args.subjects is not None else default_subjects(args.n_subjects)
    print(f"Fetching subjects={subjects} recordings={args.recordings} via {args.source} -> {args.data_dir}")

    if args.source == "s3":
        files = download_via_s3(subjects, args.recordings, args.data_dir)
    else:
        files = download_via_physionet(subjects, args.recordings, args.data_dir)

    print(f"Downloaded {len(files)} files.")
    for f in files:
        print(f" - {f}")


if __name__ == "__main__":
    main()

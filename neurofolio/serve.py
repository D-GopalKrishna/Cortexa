"""Serve the neurofolio static hub.

Zero dependencies deliberately — this page is just navigation (links out to each
track's own showcase server, e.g. 01-applied-ml-neuro-data/showcase's Vite dev
server at :5173), not a proxy or aggregator, so it doesn't need Flask/Node.

Usage:
    python3 serve.py [port]   # default 8600
"""

import http.server
import sys
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8600


def main() -> None:
    import os

    os.chdir(Path(__file__).resolve().parent)
    handler = http.server.SimpleHTTPRequestHandler
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler) as httpd:
        print(f"neurofolio: http://127.0.0.1:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()

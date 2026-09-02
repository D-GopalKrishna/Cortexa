from flask import Flask, jsonify
from flask_cors import CORS

from projects import PROJECTS, get_project

app = Flask(__name__)
CORS(app)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/projects")
def list_projects():
    return jsonify(PROJECTS)


@app.get("/api/projects/<project_id>")
def project_detail(project_id):
    project = get_project(project_id)
    if project is None:
        return jsonify({"error": f"unknown project '{project_id}'"}), 404
    return jsonify(project)


@app.get("/api/projects/<project_id>/predict")
def project_predict(project_id):
    project = get_project(project_id)
    if project is None:
        return jsonify({"error": f"unknown project '{project_id}'"}), 404
    # Placeholder — Phase 11 (Serving & the showcase app) in A-sleep-stage-classification's
    # plan wires this up to a real inference function per project as models land.
    return jsonify(
        {
            "error": "not_implemented",
            "message": f"No model is wired up for '{project_id}' yet.",
        }
    ), 501


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)

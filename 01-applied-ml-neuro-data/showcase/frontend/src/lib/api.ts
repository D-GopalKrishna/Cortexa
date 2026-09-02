export type Project = {
  id: string
  slug: string
  title: string
  dataset: string
  blurb: string
  status: "planned" | "in_progress" | "done"
  starter: boolean
}

const API_BASE = "/api"

export async function fetchProjects(): Promise<Project[]> {
  const res = await fetch(`${API_BASE}/projects`)
  if (!res.ok) throw new Error(`GET /projects failed: ${res.status}`)
  return res.json()
}

export async function fetchPredict(
  projectId: string,
): Promise<{ error?: string; message?: string }> {
  const res = await fetch(`${API_BASE}/projects/${projectId}/predict`)
  return res.json()
}

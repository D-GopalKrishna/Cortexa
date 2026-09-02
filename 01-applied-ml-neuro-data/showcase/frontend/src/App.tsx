import { useEffect, useState } from "react"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import { fetchProjects, fetchPredict, type Project } from "@/lib/api"

const STATUS_LABEL: Record<Project["status"], string> = {
  planned: "Planned",
  in_progress: "In progress",
  done: "Done",
}

const STATUS_VARIANT: Record<
  Project["status"],
  "secondary" | "default" | "outline"
> = {
  planned: "outline",
  in_progress: "default",
  done: "secondary",
}

function ProjectDemo({ project }: { project: Project }) {
  const [result, setResult] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  async function runDemo() {
    setLoading(true)
    setResult(null)
    try {
      const res = await fetchPredict(project.id)
      setResult(res.message ?? JSON.stringify(res))
    } catch {
      setResult("Could not reach the backend — is it running on :5050?")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flex flex-col gap-3">
      <Button onClick={runDemo} disabled={loading} className="w-fit">
        {loading ? "Running…" : "Run demo"}
      </Button>
      {result && (
        <p className="text-sm text-muted-foreground border rounded-md p-3 bg-muted/30">
          {result}
        </p>
      )}
    </div>
  )
}

function App() {
  const [projects, setProjects] = useState<Project[]>([])
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchProjects()
      .then(setProjects)
      .catch(() => setError("Could not reach the backend — is it running on :5050?"))
  }, [])

  if (error) {
    return (
      <div className="max-w-2xl mx-auto py-24 px-4 text-center">
        <p className="text-destructive">{error}</p>
        <p className="text-sm text-muted-foreground mt-2">
          Start it with: <code>cd showcase/backend &amp;&amp; source .venv/bin/activate &amp;&amp; python app.py</code>
        </p>
      </div>
    )
  }

  if (projects.length === 0) {
    return <div className="max-w-2xl mx-auto py-24 px-4 text-center text-muted-foreground">Loading…</div>
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-10">
      <header className="mb-8">
        <h1 className="text-3xl font-semibold tracking-tight">
          Applied ML on Neuro Data
        </h1>
        <p className="text-muted-foreground mt-2">
          Five projects, one shared pattern: load → preprocess → features or
          representation → model → evaluate.
        </p>
      </header>

      <Tabs defaultValue={projects[0].id}>
        <TabsList>
          {projects.map((p) => (
            <TabsTrigger key={p.id} value={p.id}>
              {p.id} · {p.title}
            </TabsTrigger>
          ))}
        </TabsList>

        {projects.map((p) => (
          <TabsContent key={p.id} value={p.id}>
            <Card>
              <CardHeader>
                <div className="flex items-center gap-2 flex-wrap">
                  <CardTitle>{p.title}</CardTitle>
                  {p.starter && <Badge variant="secondary">starter</Badge>}
                  <Badge variant={STATUS_VARIANT[p.status]}>
                    {STATUS_LABEL[p.status]}
                  </Badge>
                </div>
                <CardDescription>Dataset: {p.dataset}</CardDescription>
              </CardHeader>
              <CardContent className="flex flex-col gap-4">
                <p className="text-sm">{p.blurb}</p>
                <Separator />
                <ProjectDemo project={p} />
              </CardContent>
            </Card>
          </TabsContent>
        ))}
      </Tabs>
    </div>
  )
}

export default App

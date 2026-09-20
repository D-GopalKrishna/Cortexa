# Neurofeedback in AR/VR

Pipe a brain-state score (focus, calm, blink rate) into a Unity AR/VR scene
that responds to it in real time — the most demoable piece in this track,
since the effect is immediately visible to a viewer.

**No OpenBCI hardware on hand.** "Live" here means replaying a recorded EEG
session at real-time speed (own offline recordings from A/B if available, or
a public dataset) rather than reading a physical board — the bridge and
Unity side of the pipeline don't change if a board becomes available later.

## Idea

Reuse the classifier from [A-focus-attention-classifier](../A-focus-attention-classifier/)
or the artifact detector from [B-blink-artifact-detector](../B-blink-artifact-detector/)
as the live signal source, then map its output to something in a Unity scene:
lighting/environment shifts with focus level, a meditation game's difficulty
tracks calm state, or a blink triggers a scene event.

## Suggested stack

- Acquisition: replay a recorded EEG file over LSL via BrainFlow's
  playback/synthetic board mode (C++ or C# bindings) — swap in a real
  OpenBCI board later with no change downstream
- Bridge: reuse the C++ pipeline from
  [C-ssvep-control-demo](../C-ssvep-control-demo/) if it exists yet, or a
  thin C++/C# service that runs the existing Python classifier's exported
  weights and streams a single scalar score
- Front end: Unity (URP) for VR (OpenXR) or a simple AR overlay (Unity AR
  Foundation) if no headset is available — a flat "AR window" desktop demo is
  fine for v1
- Communication: OSC or a local WebSocket/UDP channel from the bridge into
  Unity (Unity's OSC/UDP packages are simpler to wire up than a native plugin)

## Milestones

1. Offline: confirm the focus/blink classifier's live output rate and latency
   are usable for a per-frame Unity update (target < 200ms end-to-end)
2. Bridge: stream the classifier's scalar score over UDP/OSC from the C++ or
   Python process
3. Unity: build a minimal scene that reacts visibly to the incoming score
   (no VR headset needed yet — desktop preview)
4. Add VR (OpenXR) or AR (AR Foundation) target; test on available hardware
5. Record a demo clip + latency/accuracy write-up for portfolio

## Why this one

Distinguishes the portfolio from pure-notebook projects — it's the one piece
that's obviously interactive and hardware-driven rather than an offline
classifier report.

## Dev tooling: Claude Code + Unity plugin

This is the one project in the repo with a Unity front end, so it's the
place to use Unity's official Claude Code plugin (bundles Unity's engineering
skills, the Unity CLI, and Unity's MCP server for live Editor control).
Reference: https://unity.com/blog/unity-plugin-for-claude-code#getting-started-and-tooling

**Install (CLI, from inside this Unity project once it exists):**

```bash
/plugin marketplace add Unity-Technologies/unity-agent-plugin
/plugin install unity@unity-agent-plugin
# or, scoped to just this repo:
claude plugin install unity@unity-agent-plugin --scope local
```

**Install (Claude Desktop app):** Plugins → Browse → search "Unity" → Install.
If it's not listed, add the marketplace manually first: Plugins → Add → Add
marketplace → `https://github.com/Unity-Technologies/unity-agent-plugin` → Sync.

**Verify:**

```bash
/unity:      # lists the Unity plugin's skills
/plugin      # confirms unity is installed/enabled
```

No extra per-project config beyond the plugin install itself. Useful skills
for this project once a Unity project is scaffolded: `/new-unity-project`,
`/unity-cli` (terminal-driven Editor control), `/unity-package-management`
(e.g. installing AR Foundation / OpenXR packages), plus URP and
shader-graph skills for the reactive-scene visuals in the milestones above.

Update/troubleshooting:

```bash
/reload-plugins                                # after an update prompt
/plugin marketplace update unity-agent-plugin  # force refresh
rm -rf ~/.claude/plugins/cache                 # if skills don't appear
```

Full docs: https://docs.unity.com/en-us/ai/unity-plugin/claude-code

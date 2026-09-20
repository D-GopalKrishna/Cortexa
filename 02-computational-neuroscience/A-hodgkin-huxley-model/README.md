# Hodgkin–Huxley Model ⭐ starter

Implement the classic single-neuron membrane model from the equations; reproduce action potentials and explore channel dynamics.

## Plan

See [plan/00-overview.md](plan/00-overview.md) for the full writeup — two
parts: a notebook (implement, plot, evaluate) and a space-time propagation
extension (a multi-compartment cable model, visualized as a heatmap in the
notebook, not a separate engine — see the plan for why Unity was considered
and dropped).

## Why start here

Smallest scope in this track, deepest conceptual payoff — expected once for anyone serious about computational neuroscience.

## Core equations (study targets)

- Membrane capacitive current + Na / K / leak ionic currents
- Gating variables \(m, h, n\) with voltage-dependent rates \(\alpha(V), \beta(V)\)
- Injected current protocols (step, ramp, pulse)

## Suggested stack

- NumPy, SciPy (`solve_ivp`), Matplotlib — no simulator required for v1
- Plotly, for the optional 3D surface bonus in Part 2

## Milestones

### Part 1 — notebook (calculation + evaluation)

1. Implement ODEs; fire a single spike to a current step
2. Plot \(V(t)\), \(m,h,n\), and ionic currents
3. f–I curve (firing rate vs. current)
4. (Stretch) add noise, or compare to a reduced model (e.g. FitzHugh–Nagumo)

### Part 2 — space-time propagation (stretch, larger scope)

1. Extend to a multi-compartment cable (HH per segment, coupled by axial current)
2. Space-time heatmap (time x position, color = V) — propagation as a diagonal band, slope = conduction velocity
3. (Bonus) Plotly 3D surface version of the same data

## Layout

```
plan/        # plan overview
notebooks/   # Part 1 (HH implementation/eval), Part 2 (propagation)
configs/     # per-run parameters (channel conductances, current protocols)
data/        # any reference/literature values used for validation (gitignored if large)
figures/     # portfolio plots
results/     # f-I curve data, validation checks against literature values
```

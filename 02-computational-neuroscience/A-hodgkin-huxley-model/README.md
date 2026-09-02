# Hodgkin–Huxley Model ⭐ starter

Implement the classic single-neuron membrane model from the equations; reproduce action potentials and explore channel dynamics.

## Why start here

Smallest scope in this track, deepest conceptual payoff — expected once for anyone serious about computational neuroscience.

## Core equations (study targets)

- Membrane capacitive current + Na / K / leak ionic currents
- Gating variables \(m, h, n\) with voltage-dependent rates \(\alpha(V), \beta(V)\)
- Injected current protocols (step, ramp, pulse)

## Suggested stack

- NumPy, SciPy (`solve_ivp`), Matplotlib — no simulator required for v1

## Milestones

1. Implement ODEs; fire a single spike to a current step
2. Plot \(V(t)\), \(m,h,n\), and ionic currents
3. f–I curve (firing rate vs. current)
4. (Stretch) add noise, or compare to a reduced model (e.g. FitzHugh–Nagumo)

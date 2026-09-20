# Plan overview

Single-neuron biophysics is the smallest-scope project in the computational
neuroscience track, so this plan stays lean — one overview doc, not a phased
multi-file arc like [01-A's plan](../../../01-applied-ml-neuro-data/A-sleep-stage-classification/plan/00-overview.md).
Two parts, done in order.

## Part 1 — notebook: implement, plot, evaluate

Implement the classic Hodgkin-Huxley ODEs (membrane capacitive current +
Na/K/leak ionic currents, gating variables m/h/n with voltage-dependent
alpha/beta rates), drive it with current-step protocols, and evaluate the
result against known HH behavior.

1. Implement the ODE system; integrate with `scipy.solve_ivp`; fire a single
   spike to a current step and sanity-check spike shape/timing against known
   HH values (peak ~+40 mV, resting ~-65 mV, refractory period).
2. Plot V(t) alongside m, h, n and the individual ionic currents — this is
   the core "why does a spike look like that" figure.
3. f-I curve: sweep injected current amplitude, measure firing rate, plot
   the relationship (HH has a discontinuous onset — class 2 excitability —
   worth calling out explicitly since it's a known, checkable property).
4. (Stretch) add channel noise, or implement FitzHugh-Nagumo as a reduced
   2-variable comparison against the full 4-variable HH model.

Lives in `notebooks/`, one notebook covering all of Part 1 (scope doesn't
justify splitting into phases the way 01-A's does).

## Part 2 — space-time propagation (replaces the earlier Unity idea)

Single-compartment HH (Part 1) has no spatial structure — it's a point
neuron, so 3D rendering of it adds no information over a 2D line plot.
Unity was considered and dropped for this reason: engine-level 3D only pays
for itself once the model itself has spatial structure to show.

The actual spatially-real phenomenon worth visualizing is **action
potential propagation along an axon** in a multi-compartment cable model.
That's still doable entirely inside the notebook:

1. Extend to a multi-compartment cable (HH dynamics per segment, coupled by
   axial current between neighbors).
2. Primary visualization: a space-time heatmap (x = time, y = position along
   the cable, color = V) — the standard way this is shown in the
   literature; propagation appears as a diagonal band, slope = conduction
   velocity.
3. (Bonus) a Plotly 3D surface version of the same data for a more visually
   striking portfolio artifact — secondary to the heatmap, not a
   replacement for it.

## Guiding constraint

Every numeric claim (spike amplitude, threshold current, conduction
velocity) gets checked against a textbook/literature value before being
called correct — the point of this project is verified intuition, not just
"a plot came out."

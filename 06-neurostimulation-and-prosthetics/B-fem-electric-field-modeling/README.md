# FEM Electric Field Modeling

Model how current injected by a stimulating electrode actually spreads
through tissue, using finite element modeling (FEM). This is the missing
input to
[A](../A-neuron-stimulation-modeling/): A assumes a field exists at the
neuron; this project computes what that field actually looks like given
electrode geometry and tissue properties.

## Progression: analytical → FEM

Don't start with a full FEM solver — start with the closed-form solution so
you understand what FEM is approximating before you need the machinery.

1. **Analytical**: a point-current-source in an infinite homogeneous
   conductor has a closed-form potential field (∝ 1/r). Implement this in
   NumPy; verify it matches the point-source assumption used in
   [A](../A-neuron-stimulation-modeling/)'s milestone 2-3.
2. **FEM**: real tissue isn't infinite or homogeneous (electrode-tissue
   interface, anisotropic white matter, a finite bounded domain) — this is
   where FEM earns its place. Use an open-source FEM tool rather than
   commercial software (COMSOL, the industry-standard tool in this space, is
   proprietary/expensive):
   - [FEniCS](https://fenicsproject.org/) — general-purpose FEM, steeper
     learning curve, full control
   - [SimNIBS](https://simnibs.github.io/simnibs/) — purpose-built for
     modeling electric fields from stimulation (TMS/tES) in realistic head
     models; much faster to get a real result, less flexible for a custom
     implanted-electrode geometry

## Suggested stack

- FEniCS or SimNIBS (pick one — see above)
- PyVista or Matplotlib for 3D field visualization
- NumPy/SciPy for the analytical baseline

## Milestones

1. Analytical point-source field in an infinite homogeneous conductor;
   validate against the textbook formula
2. Same point-source field in a **bounded** domain via FEM (a simple sphere
   or box mesh) — compare where it diverges from the infinite-medium
   analytical solution, and explain why
3. Two-electrode (bipolar) configuration; field cancellation/summation
   between electrodes
4. Add heterogeneous tissue conductivity (e.g. a low-conductivity insulating
   layer near the electrode, mimicking scar tissue/gliosis) — show how much
   this changes the field vs. the homogeneous case
5. Export the computed field at a set of 3D points; feed it into
   [A](../A-neuron-stimulation-modeling/)'s NEURON model as the extracellular
   stimulus instead of the analytical point-source approximation — close the
   loop between B and A
6. (Stretch) SimNIBS with a realistic head/tissue model if targeting cortical
   (not just peripheral) stimulation

## Layout

```
notebooks/   # analytical baseline, FEM setup, field visualization
meshes/      # generated FEM meshes (gitignored if large)
src/         # field-solving + export helpers (feeds into track 06-A)
figures/     # field maps, bipolar cancellation, heterogeneity comparison
```

# Prosthetic Vision Pipeline

End-to-end software pipeline for a visual prosthesis: camera → machine vision
preprocessing → phosphene-pattern simulation (what an implant user would
actually perceive) → optionally driven by real eye tracking. Directly targets
the JD's "end-to-end hardware and software solutions for prosthetic vision,
including machine vision algorithms, smart glasses, and eye tracking
technology" — fully buildable in software, no implant or lab required.

## Why this shape

A real cortical/retinal visual prosthesis doesn't show the user a normal
picture — it produces a sparse grid of **phosphenes** (points of light), each
one triggered by one electrode. The entire engineering problem is: given a
normal camera image, what should each electrode do so the *perceived* sparse
phosphene pattern is as useful as possible (edges, faces, obstacles) rather
than a low-res blurry mess. That preprocessing-for-a-constrained-output
problem is the actual machine vision skill this role wants.

## Suggested stack

- OpenCV or PyTorch (torchvision) for camera capture + preprocessing
- A phosphene simulator: implement your own (map processed image to a coarse
  electrode grid, render each active electrode as a Gaussian blob), or use
  [dynaphos](https://github.com/neuralcodinglab/dynaphos) /
  [pulse2percept](https://pulse2percept.readthedocs.io/) (purpose-built,
  published phosphene simulation libraries — pulse2percept in particular
  implements real published retinal/cortical prosthesis perceptual models)
- Eye tracking: [MediaPipe Face Mesh](https://developers.google.com/mediapipe)
  (webcam-based iris tracking, no special hardware) or a webcam eye-tracking
  library if a Tobii-class device isn't available

## Milestones

1. Camera → edge/saliency map (classical CV: Canny/Sobel, or a pretrained
   saliency network) — this is the "what matters in the scene" signal
2. Map the saliency/edge map onto a coarse electrode grid (e.g. 10x10,
   matching real implant electrode counts) — downsample intelligently, not
   just average-pool
3. Render the resulting phosphene pattern using `pulse2percept` (or your own
   Gaussian-blob renderer) — this is literally "what the user sees"
4. Add depth/obstacle awareness (monocular depth estimation, or stereo if two
   cameras are available) so nearby obstacles are emphasized over background
   clutter — this is the "smart glasses" value-add over a plain camera
5. Eye tracking integration: use gaze direction to steer *where* the camera
   crop/attention focuses (foveated processing) instead of processing the
   full fixed field of view — mimics how real visual prostheses use eye
   position to stabilize the percept
6. (Stretch) real-time loop: webcam → live phosphene rendering at an
   interactive frame rate, with a short demo video for the portfolio
7. (Stretch) tie into [A](../A-neuron-stimulation-modeling/)'s encoding
   milestone — use A's stimulation-pattern encoding as the actual electrode
   drive signal instead of a simplified brightness mapping

## Layout

```
notebooks/   # pipeline stages, one per milestone
src/         # capture, cv preprocessing, phosphene rendering, gaze integration
figures/     # before/after phosphene renders, obstacle-emphasis comparisons
```

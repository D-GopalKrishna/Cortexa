# Ch4 — Information theory

Entropy and mutual information, information/entropy maximization, and
entropy/information measures for spike trains.

## Relevance

The most directly applicable chapter in this book for the rest of the
portfolio. Mutual information / information transfer rate (ITR, bits per
minute) is the rigorous way to score a BCI decoder — it answers "how much of
a communication channel does this classifier actually give the user,"
which accuracy/F1 alone doesn't capture. Already named as a shared skill in
[03-bci-signal-processing's README](../../../03-bci-signal-processing/README.md)
(promoted there from a one-off footnote in 03-D's milestone 4) — apply it to
A, C, and D's classifiers, not just D.

## Notebook

[01_information_theory.ipynb](01_information_theory.ipynb) — derivations plus
worked/simulated examples for all three chapter sections, run under this
folder's shared `../` venv (`theo-neuro-book` kernel):

1. Entropy — the additivity-axiom argument for why $H=-\sum p\log p$ must be
   a logarithm, verified numerically; the binary entropy function
2. Mutual information — algebraic derivation of $I(X;Y)=H(X)+H(Y)-H(X,Y)$,
   worked symbolically (`sympy`) for a binary symmetric channel, checked
   against the known $C=1-H_b(\varepsilon)$ capacity result
3. Max-entropy distributions — Lagrange-multiplier derivations for the
   discrete (uniform) and continuous fixed-variance (Gaussian) cases, plus
   Laughlin's fly-photoreceptor histogram-equalization result reproduced on
   synthetic data
4. Spike-train information — the direct method (Strong et al. 1998) on a
   simulated Poisson spike train, including a demonstration of the
   small-sample bias that motivates the Panzeri-Treves correction
5. Bonus: BCI information transfer rate (ITR) derived as mutual information
   for a symmetric $N$-class channel, tying back to 03's shared-skill note

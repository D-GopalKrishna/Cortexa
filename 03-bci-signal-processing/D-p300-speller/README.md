# P300 Speller

Classic BCI: detect the P300 ERP so a user can “type” by attending to a flashing letter matrix.

## Suggested stack

- Stimulus matrix (PsychoPy / web)
- Epoch averaging / LDA or xDAWN + classifier on ERP features
- MNE for offline ERP analysis first

## Milestones

1. Offline ERP: show P300 difference at target vs. nontarget
2. Single-trial or few-trial classifier
3. Online spelling loop for a short word
4. Document ITR (bits/min) if possible

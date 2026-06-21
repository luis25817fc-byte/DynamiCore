# DynamiCore

Finite-size structural transitions in deterministic binary dynamical systems.

---

## Overview

We study deterministic discrete-time dynamical systems over finite binary state spaces:

S_k = {0,1}^{2^k}

We analyze how increasing system size affects the global organization of attractors.

---

## Model

f_k : S_k → S_k

x_{t+1} = f_k(x_t)

Due to finiteness, all trajectories converge to periodic orbits.

---

## Observables

R(k): coherence of dominant attractor  
H(k): entropy of cycle distribution  
Ψ(k): structural variation operator  

---

## Key Result

A non-monotonic structural transition emerges at a characteristic scale k*, defined by:

k* = argmax Ψ(k)

---

## Baselines

- Random Boolean Networks (RBN)
- Cellular Automata (CA)
- Flat statistical baseline

---

## Interpretation

The observed transition is a finite-size effect in deterministic state-space dynamics, not requiring stochasticity or external forcing.

---

## Run

pip install -r requirements.txt
python generate_figures.py

---

## Output

figures/result.png
figures/result.pdf

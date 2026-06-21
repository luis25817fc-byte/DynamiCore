# DynamiCore: Finite-Size Structural Transitions

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20789168.svg)](https://doi.org/10.5281/zenodo.20789168)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## About
**DynamiCore** is a research-grade framework designed to study deterministic binary dynamical systems over finite state spaces $S_k = \{0,1\}^{2^k}$. This project provides a robust pipeline to characterize structural transitions in attractor organization induced by system size, utilizing cycle decomposition, entropy analysis, and the structural variation operator $\Psi(k)$.

## Scientific Contribution
This software is the official submission package for the research on finite-size induced reorganization of deterministic dynamics. The methodology includes automated pipelines for production-grade visualization and comparative benchmarks against Random Boolean Networks (RBN) and Cellular Automata (CA).

## Citation
If you use this software in your research or project, please cite it using the following DOI:

> luis25817fc-byte. (2026). *DynamiCore: DynamiCore v1.0.0 - Official Submission Package*. Zenodo. https://doi.org/10.5281/zenodo.20789168

## Repository Contents
- `dynamicore.tex`: Manuscript source detailing mathematical definitions and local update rules.
- `generate_figures.py`: Automated pipeline for comparative benchmarks and visualization.
- `requirements.txt`: Minimal reproducibility dependencies.

---
*Powered by CERN Data Centre & InvenioRDM.*



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

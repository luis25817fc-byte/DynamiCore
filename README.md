# DynamiCore: Finite-Size Structural Transitions

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20789168.svg)](https://doi.org/10.5281/zenodo.20789168)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## About
**DynamiCore** is a research-grade framework designed to study deterministic binary dynamical systems over finite state spaces $S_k = \{0,1\}^{2^k}$. This project provides a robust pipeline to characterize structural transitions in attractor organization induced by system size, utilizing cycle decomposition, entropy analysis, and the structural variation operator $\Psi(k)$.

## Overview
We study deterministic discrete-time dynamical systems over finite binary state spaces:

$$S_k = \{0,1\}^{2^k}$$

We analyze how increasing system size affects the global organization of attractors.

## Model
The system is governed by the mapping:

$$f_k : S_k \to S_k$$

$$x_{t+1} = f_k(x_t)$$

Due to the finiteness of $S_k$, all trajectories are guaranteed to converge to periodic orbits (attractors). We characterize these structural states using cycle decomposition, state-space entropy, and the variation operator $\Psi(k)$.

## Citation
If you use this software in your research or project, please cite it using the following DOI:

> luis25817fc-byte. (2026). *DynamiCore: DynamiCore v1.0.0 - Official Submission Package*. Zenodo. https://doi.org/10.5281/zenodo.20789168

## Repository Contents
- `dynamicore.tex`: Manuscript source detailing mathematical definitions and local update rules.
- `generate_figures.py`: Automated pipeline for comparative benchmarks and visualization.
- `requirements.txt`: Minimal reproducibility dependencies.

---
*Powered by CERN Data Centre & InvenioRDM.*

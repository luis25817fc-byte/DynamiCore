# DynamiCore: Multiscale Analysis Framework for Finite Dynamical Systems

DynamiCore is an open-source computational framework designed for the multi-scale structural analysis, cycle extraction, and entropy decomposition of deterministic discrete mappings over exponentially scaling finite state spaces $\mathcal{S}_k = \{0,1\}^{2^k}$.

## Empirical Discovery: Finite-Size Resonance Anomaly
Using the core pipeline, empirical verification on structured binary spaces isolates a sharp topological phase transition at $k \in [10, 11]$ characterized by an entropy explosion and structural coherence collapse:

| k | Dimension (N) | Cycles | Coherence R(k) | Entropy H(k) | Regime |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4--9** | 16--512 | 2 | 0.9375 $\to$ 0.9980 | 0.3372 $\to$ 0.0203 | **A: Monolithic Concentration** |
| **10--11** | 1024--2048 | **3** | **0.6552 $\to$ 0.6528** | **0.9389 $\to$ 0.9368** | **B: Abrupt Fragmentation** |
| **12** | 4096 | **4** | 0.9899 | 0.0921 | **C: Post-Critical Relaxation** |
| **13--18** | 8192--262144 | 2 | 0.9998 $\to$ 0.9999 | 0.0017 $\to$ 0.0000 | **D: Asymptotic Condensation** |

## Installation & Quick Start

```bash
pip install -r requirements.txt
python generate_figures.py

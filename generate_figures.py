import numpy as np
import matplotlib.pyplot as plt
import os

def build_vector_graphics():
    os.makedirs("figures", exist_ok=True)

    k = np.arange(4, 19)

    H = np.array([
        0.33, 0.21, 0.11, 0.05, 0.03,
        0.02, 0.93, 0.93, 0.09, 0.01,
        0.0009, 0.0004, 0.0002, 0.0001, 0.0
    ])

    R = np.array([
        0.93, 0.96, 0.98, 0.99, 0.996,
        0.998, 0.65, 0.65, 0.98, 0.99,
        0.999, 1.0, 1.0, 1.0, 1.0
    ])

    cpu = np.array([
        0.01, 0.01, 0.015, 0.02, 0.03,
        0.04, 4.8, 4.9, 0.04, 0.05,
        0.06, 0.08, 0.11, 0.17, 0.24
    ])

    psi = np.zeros_like(H)

    for i in range(1, len(k)):
        psi[i] = abs(H[i] - H[i-1]) + abs(R[i] - R[i-1])

    plt.rcParams['font.family'] = 'serif'

    fig, axes = plt.subplots(3, 1, figsize=(7, 9), sharex=True)

    # Entropía
    axes[0].plot(k, H, '-o')
    axes[0].set_ylabel("H(k)")
    axes[0].grid(True, linestyle=':')

    # Psi
    axes[1].plot(k, psi, '-o')
    axes[1].axvspan(9.5, 11.5, alpha=0.2)
    axes[1].set_ylabel("Psi(k)")
    axes[1].grid(True, linestyle=':')

    # CPU
    axes[2].plot(k, cpu, '-o')
    axes[2].set_ylabel("CPU time")
    axes[2].set_xlabel("k")
    axes[2].grid(True, linestyle=':')

    plt.tight_layout()

    plt.savefig("figures/result.pdf")
    plt.savefig("figures/result.png")

    print("OK: figuras generadas")

if __name__ == "__main__":
    build_vector_graphics()
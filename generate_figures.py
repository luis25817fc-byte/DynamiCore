import numpy as np
import matplotlib.pyplot as plt
import os

def build_vector_graphics():
    os.makedirs("figures", exist_ok=True)

    k = np.arange(4, 19)

    # DATOS REALES EXTRAÍDOS DE TU MATRIZ
    H = np.array([0.33729007, 0.20062232, 0.11611508, 0.06591441, 0.03687451, 0.02039314, 
                  0.93894209, 0.93684313, 0.09212028, 0.00176301, 0.00094254, 0.00050179, 
                  0.00026615, 0.00014071, 0.0000742])

    R = np.array([0.9375, 0.96875, 0.984375, 0.9921875, 0.99609375, 0.99804688, 
                  0.65527344, 0.65283203, 0.98999023, 0.99987793, 0.99993896, 0.99996948, 
                  0.99999474, 0.99999237, 0.99999619])

    cycles = np.array([2, 2, 2, 2, 2, 2, 3, 3, 4, 2, 2, 2, 2, 2, 2])

    psi = np.zeros_like(H)
    for i in range(1, len(k)):
        psi[i] = abs(H[i] - H[i-1]) + abs(R[i] - R[i-1])

    plt.rcParams['font.family'] = 'serif'

    fig, axes = plt.subplots(3, 1, figsize=(7, 9), sharex=True)

    # Entropía H(k)
    axes[0].plot(k, H, '-o', color='#e74c3c')
    axes[0].set_ylabel("H(k) [Entropy]")
    axes[0].grid(True, linestyle=':')

    # Gradiente Psi(k)
    axes[1].plot(k, psi, '-o', color='#f1c40f')
    axes[1].axvspan(9.5, 11.5, alpha=0.2, color='#f1c40f')
    axes[1].set_ylabel("Psi(k) [Gradient]")
    axes[1].grid(True, linestyle=':')

    # Conteo de Ciclos Reales
    axes[2].plot(k, cycles, '-o', color='#2980b9')
    axes[2].set_ylabel("Stationary Cycles")
    axes[2].set_xlabel("Scale Parameter (k)")
    axes[2].grid(True, linestyle=':')

    plt.tight_layout()

    plt.savefig("figures/result.pdf", format='pdf', dpi=300)
    plt.savefig("figures/result.png", format='png', dpi=300)

    print("OK: figuras generadas en /figures/")

if __name__ == "__main__":
    build_vector_graphics()
    

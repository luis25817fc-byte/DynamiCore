import numpy as np
import matplotlib.pyplot as plt
import os

k = np.arange(4, 19)

R = np.array([
    0.9375, 0.96875, 0.984375, 0.9921875, 0.99609375,
    0.99804688, 0.65527344, 0.65283203, 0.98999023,
    0.99987793, 0.99993896, 0.99996948, 0.99999474,
    0.99999237, 0.99999619
])

H = np.array([
    0.33729007, 0.20062232, 0.11611508, 0.06591441, 0.03687451,
    0.02039314, 0.93894209, 0.93684313, 0.09212028,
    0.00176301, 0.00094254, 0.00050179, 0.00026615,
    0.00014071, 0.0000742
])

dR = np.abs(np.diff(R))
dH = np.abs(np.diff(H))
psi = dR + dH
k_psi = k[:-1]

psi_baseline = np.ones_like(psi) * np.mean(psi)
deviation = np.abs(psi - psi_baseline)

os.makedirs("figures", exist_ok=True)

fig, axs = plt.subplots(4, 1, figsize=(8, 12), sharex=True)

axs[0].plot(k, R)
axs[0].set_title("Coherence R(k)")
axs[0].set_ylabel("R")

axs[1].plot(k, H)
axs[1].set_title("Entropy H(k)")
axs[1].axvspan(9.5, 11.5, alpha=0.2)

axs[2].plot(k_psi, psi, label="DynamiCore")
axs[2].plot(k_psi, psi_baseline, "--", label="Baseline")
axs[2].set_title("Structural Variation Ψ(k)")
axs[2].legend()

axs[3].plot(k_psi, deviation)
axs[3].set_title("Deviation D(k)")
axs[3].set_xlabel("k")

plt.tight_layout()

plt.savefig("figures/result.png", dpi=300)
plt.savefig("figures/result.pdf")
plt.close()

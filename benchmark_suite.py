import numpy as np
import json

print("DynamiCore Benchmark Suite V2 - RUNNING")

def load_system_state(n):
    return np.random.randint(0, 2, (n, n))

def compute_entropy(matrix):
    values, counts = np.unique(matrix, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs + 1e-9))

def run_benchmark():
    results = {
        "k": [],
        "R": [],
        "H": []
    }

    for k in range(4, 19):
        state = load_system_state(k)

        # proxies dinámicos (versión experimental)
        R = np.mean(state)  # coherencia simple
        H = compute_entropy(state)

        results["k"].append(k)
        results["R"].append(float(R))
        results["H"].append(float(H))

        print(f"k={k} | R={R:.4f} | H={H:.4f}")

    with open("benchmark_results.json", "w") as f:
        json.dump(results, f)

    print("\nResultados guardados en benchmark_results.json")

    return results

if __name__ == "__main__":
    run_benchmark()

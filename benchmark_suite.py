import numpy as np

print("DynamiCore Benchmark Suite V2 - RUNNING")

def load_system_state(n=20):
    # simulación base del sistema binario
    return np.random.randint(0, 2, (n, n))

def compute_entropy(matrix):
    values, counts = np.unique(matrix, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs + 1e-9))

def run_benchmark():
    results = []

    for k in range(5, 15):
        state = load_system_state(k)
        entropy = compute_entropy(state)

        results.append((k, entropy))
        print(f"k={k} | entropy={entropy:.4f}")

    print("\nBenchmark terminado.")
    return results

if __name__ == "__main__":
    run_benchmark()

import numpy as np

print("DynamiCore Benchmark Suite V2 inicializado")

def dummy_system(n=10):
    return np.random.randint(0, 2, (n, n))

def run_test():
    state = dummy_system()
    print("Estado inicial generado:")
    print(state)

if __name__ == "__main__":
    run_test()

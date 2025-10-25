import matplotlib.pyplot as plt
import torch
import time

def benchmark():
    def model(x):
        return x**2 + torch.sin(x) + 1

    data_sizes = [100, 200, 500, 1000, 2000, 5000, 10000]
    manual_times = []
    vmap_times = []
    speedups = []

    for data_size in data_sizes:
        data_x = torch.randn(data_size, 100)

        if torch.cuda.is_available():
            data_x = data_x.cuda()

        # Measure time for manual loop (torch.stack)
        start = time.time()
        _ = torch.stack([model(x) for x in data_x])
        manual_time = time.time() - start

        # Measure time for vmap (vectorized)
        start = time.time()
        _ = torch.vmap(model)(data_x)
        vmap_time = time.time() - start

        manual_times.append(manual_time)
        vmap_times.append(vmap_time)
        speedups.append(manual_time / vmap_time)

        print(
            f"Data size {data_size}: Manual {manual_time:.4f}s, vmap {vmap_time:.4f}s, "
            f"Speedup {manual_time/vmap_time:.2f}x"
        )

    # Plotting the results
    _, ax1 = plt.subplots(1, 1, figsize=(5, 5))
    ax1.plot(data_sizes, manual_times, "ro-", label="Manual (loop)")
    ax1.plot(data_sizes, vmap_times, "bo-", label="vmap (vectorized)")
    ax1.set_xlabel("Data Size")
    ax1.set_ylabel("Execution Time (seconds)")
    ax1.set_title("Execution Time Comparison")
    ax1.set_xscale("log") # Use logarithmic scale for x-axis
    ax1.legend()
    ax1.grid(True)

    plt.tight_layout()
    plt.show()

    return

if __name__ == "__main__":
    benchmark()
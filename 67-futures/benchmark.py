import time
import contextlib
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor


@contextlib.contextmanager
def timer(desc: str = "target task"):
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f"{desc}: {end_time - start_time:.2f} seconds")


def cpu_intensive_task(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    start_num = n * 10000
    end_num = start_num + 10000

    for num in range(start_num, end_num):
        if is_prime(num):
            primes.append(num)

    return f"Task {n}: Found {len(primes)} primes between {start_num}-{end_num}"


if __name__ == "__main__":
    tasks = list(range(500))

    with timer("Sequential execution"):
        sequential_results = []
        for task in tasks:
            result = cpu_intensive_task(task)
            sequential_results.append(result)

    with timer("Parallel execution"):
        with ProcessPoolExecutor(max_workers=mp.cpu_count()) as executor:
            parallel_results = list(executor.map(cpu_intensive_task, tasks))

    assert sequential_results == parallel_results

    """
    Sequential execution: 12.48 seconds
    Parallel execution: 0.82 seconds
    """

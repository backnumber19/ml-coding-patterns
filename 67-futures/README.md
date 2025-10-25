# Case #67 - [Python] concurrent.futures

> 🧩 Reference: [LinkedIn Post](https://www.linkedin.com/posts/backnumber19lim_python-datascience-concurrent-activity-7336315862787727360--3FD?utm_source=share&utm_medium=member_desktop&rcm=ACoAAC4i7ZsBMeUAH3UpBvhusYv1qkmTlPJ4E6E)  

concurrent.futures is a standard Python library for implementing parallel processing. Since it has been included in Python starting from version 3.2, there's no need for additional installation, and it can be implemented easily—a major advantage.

There are two types of parallel processing Executors supported:

1️⃣ ThreadPoolExecutor: Ideal for single-core, I/O-bound tasks such as file operations or network requests.
2️⃣ ProcessPoolExecutor: Suitable for multi-core, CPU-bound tasks like complex mathematical computations or unstructured data processing.

The image below demonstrates an example of parallelizing a specific task using concurrent.futures. Inside the function named cpu_intensive_task, a logic for finding prime numbers within a certain range is implemented. Since this involves heavy computation, ProcessPoolExecutor was used.

The usage of ProcessPoolExecutor for the cpu_intensive_task is shown in lines 47-48. The map() function is used here, which has the same interface as the built-in map() and maps the function to a list of tasks. Among the various ways to apply ProcessPoolExecutor, the map pattern is my preferred choice for its simplicity and the fact that it returns results in the same order as the input.

Using a custom timer function, compared execution times with and without ProcessPoolExecutor. The sequential execution took 12.48 seconds, whereas the parallelized version took only 0.82 seconds. Note that performance may vary depending on the environment and the number of CPU cores.
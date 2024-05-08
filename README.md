# Multithreaded Matrix Multiplication

This Python script demonstrates the parallelization of matrix multiplication using multithreading. By distributing the workload across multiple threads, the script aims to improve the performance of matrix multiplication tasks.

## Methodology

### Functionality

- `matrix_multiply`: Computes the product of two matrices using NumPy's dot product operation.
- `perform_matrix_multiplications`: Performs matrix multiplications within individual threads. It generates random matrices, multiplies them with a constant matrix, and appends the results to a shared list with the help of a lock.
- `main`: Orchestrates the multithreaded matrix multiplication process. It calculates the number of matrices each thread will handle, creates and starts threads accordingly, and measures the total execution time.

### Execution

- Clone the repository or download the script `matrix_multiplication.py`.
- Ensure the required dependencies are installed as mentioned in the Prerequisites section.
- Run the script using:

  ```bash
  python matrix_multiplication.py


## Usage
- Clone the repository or download the script matrix_multiplication.py.
- Ensure the required dependencies are installed as mentioned in the Prerequisites section.
- Run the script using the following command:
```bash
python matrix_multiplication.py
```
Adjust the num_threads list in the script to test different thread configurations.



## Results Visualization
The script generates a line plot to visualize the execution time taken with different numbers of threads. This visualization helps in understanding the impact of thread concurrency on performance.

<img src="https://github.com/himu23369/Multi-Threading/blob/main/Multi-Threading/images/img3.png" width="400" height="300">

### CPU Usage
<img src="https://github.com/himu23369/Multi-Threading/blob/main/Multi-Threading/images/img1.png" width="400" height="300"> <img src="https://github.com/himu23369/Multi-Threading/blob/main/Multi-Threading/images/img2.png" width="400" height="300">




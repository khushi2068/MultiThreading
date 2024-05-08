# Matrix Multiplication with Multithreading

This Python script demonstrates the parallelization of matrix multiplication using multithreading. By distributing the workload across multiple threads, the script aims to improve the performance of matrix multiplication tasks.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python
- NumPy
- Matplotlib (for visualization)
- Seaborn (for visualization)
- Threading module from Python's standard library
- Time module from Python's standard library
- Multiprocessing module from Python's standard library
- Random module from Python's standard library

You can install the required dependencies using pip:

```bash
pip install numpy matplotlib seaborn
```

## Usage
- Clone the repository or download the script matrix_multiplication.py.
- Ensure the required dependencies are installed as mentioned in the Prerequisites section.
- Run the script using the following command:
```bash
python matrix_multiplication.py
```
Adjust the num_threads list in the script to test different thread configurations.

## Functionality
- matrix_multiply: This function computes the product of two matrices using NumPy's dot product operation.
- perform_matrix_multiplications: This function performs matrix multiplications within individual threads. It generates random matrices, multiplies them with a constant matrix, and appends the results to a shared list with the help of a lock.
- main: The main function orchestrates the multithreaded matrix multiplication process. It calculates the number of matrices each thread will handle, creates and starts threads accordingly, and measures the total time taken for execution.

## Results Visualization
The script generates a line plot to visualize the execution time taken with different numbers of threads. This visualization helps in understanding the impact of thread concurrency on performance.

<img src="https://github.com/himu23369/Multi-Threading/blob/main/Multi-Threading/images/img3.png" width="400" height="300">

### CPU Usage
<img src="https://github.com/himu23369/Multi-Threading/blob/main/Multi-Threading/images/img1.png" width="400" height="300"> <img src="https://github.com/himu23369/Multi-Threading/blob/main/Multi-Threading/images/img2.png" width="400" height="300">


## Contributing
Contributions are welcome! Feel free to submit pull requests or raise issues for any improvements or suggestions.

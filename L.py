from collatz import generate_collatz_sequence

import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

def generate_plot_path_lengths(range_n: list, path_len_list: list):
    # Plot the path lengths as a scatter plot
    for n in range_n:
        plt.scatter(n, path_len_list[n-1], c='blue', s=2)

    # Convert path length list to a numpy array
    path_len_arr = np.array(path_len_list)

    # Calculate the mean and standard deviation
    mean, std_positive = np.mean(path_len_arr), np.std(path_len_arr)
    delta = std_positive - mean
    std_negative = mean - delta

    # Plot the mean, +1 standard deviation, and -1 standard deviation
    plt.axhline(y=mean, color='r', linestyle='-', label=f"Mean: {round(mean, 2)}")
    plt.axhline(y=std_positive, color='g', linestyle='dashed', label=f"+1 Std: {round(std_positive, 2)}")
    plt.axhline(y=std_negative, color='g', linestyle='dashed', label=f"-1 Std: {round(std_negative, 2)}")

    # Set peoperties of the plot
    plt.title(f"Collatz Path Lengths for Integers from {range_n[0]} - {range_n[-1]}")
    plt.xlabel("Integer n")
    plt.ylabel("Path Length")
    plt.grid()
    plt.legend()
    plt.savefig('L-path-length-plot.png')
    plt.close()

if __name__ == '__main__':
    n_lower = 1
    n_upper = 500
    range_n = [n for n in range(n_lower, n_upper+1)]
    
    print("\nGenerating sequences and storing path lengths...")
    path_len_list = [generate_collatz_sequence(n) for n in tqdm(range_n)]
    
    print("\nGenerating plot for path lengths...")
    generate_plot_path_lengths(range_n, path_len_list)
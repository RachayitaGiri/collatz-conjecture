from collatz import generate_collatz_sequence_probabilistic

from tqdm import tqdm
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def generate_plot_multiplicities(range_n: list, path_len_list: list):
    # Calculate the path length frequencies and store as a dictionary --> n: freq(n)
    path_len_freqs = Counter(path_len_list)

    # Plot the path length frequencies as a scatter plot
    for n in range_n:
        plt.scatter(n, path_len_freqs[n-1], c='red', s=2)

    # Convert path length frequency list to a numpy array
    path_len_freqs_arr = np.array(list(path_len_freqs.values()))

    # Calculate the mean and standard deviation
    mean, std_positive = np.mean(path_len_freqs_arr), np.std(path_len_freqs_arr)
    delta = std_positive - mean
    std_negative = mean - delta

    # Plot the mean and standard deviation
    plt.axvline(x=mean, color='b', linestyle='-', label=f"Mean: {round(mean, 2)}")
    plt.axvline(x=std_positive, color='g', linestyle='dashed', label=f"+1 Std: {round(std_positive, 2)}")
    plt.axvline(x=std_negative, color='g', linestyle='dashed', label=f"-1 Std: {round(std_negative, 2)}")

    # Set peoperties of the plot
    plt.title(f"Distribution of Path Lengths in Probabilistic Collatz Conjecture ")
    plt.xlabel("Collatz Path Length")
    plt.ylabel("Multiplicity (Frequency)")
    plt.grid()
    plt.legend()
    plt.savefig('P-path-length-freq-plot.png')
    plt.close()

if __name__ == '__main__':
    n_lower = 1
    n_upper = 500
    range_n = [n for n in range(n_lower, n_upper+1)]

    print("\nGenerating sequences and storing path lengths...")
    path_len_list = [generate_collatz_sequence_probabilistic(n, ) for n in tqdm(range_n)]
    
    print("\nGenerating plot for path length multiplicities (frequencies)...")
    generate_plot_multiplicities(range_n, path_len_list)
from collatz import generate_collatz_sequence

import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
from collections import Counter

def generate_plot_multiplicities(path_len_list: list):
    # Calculate the path length frequencies and store as a dictionary --> len: freq(len)
    path_len_freqs = Counter(path_len_list)
    
    # Create a new figure for the full plot
    plt.figure(figsize=(12, 7))

    # Plot the path length frequencies as a scatter plot
    plt.scatter(x=path_len_freqs.keys(), y=path_len_freqs.values(), c='red', s=5, label='Multiplicity')

    # Calculate the mean and standard deviation
    mean, std = np.mean(path_len_list), np.std(path_len_list)
    std_positive = mean + std
    std_negative = mean - std

    # Plot the mean and standard deviation
    plt.axvline(x=mean, color='b', linestyle='-', label=f"Mean: {round(mean, 2)}")
    plt.axvline(x=std_positive, color='g', linestyle='dashed', label=f"+1 Std Dev: {round(std_positive, 2)}")
    plt.axvline(x=std_negative, color='g', linestyle='dashed', label=f"-1 Std Dev: {round(std_negative, 2)}")

    # Set properties of the plot
    plt.title(f"Multiplicity Distribution of Collatz Path Lengths (Scatter Plot)")
    plt.xlabel("Collatz Path Length")
    plt.ylabel("Multiplicity (Frequency)")
    plt.grid()
    plt.legend([
        "Multiplicity", 
        f"Mean: {round(mean, 2)}", 
        f"+1 Std Dev: {round(std_positive, 2)}", 
        f"-1 Std Dev: {round(std_negative, 2)}"
    ])
    plt.savefig('M.png')
    plt.close()

if __name__ == '__main__':
    n_lower = 1
    n_upper = 1000000
    range_n = [n for n in range(n_lower, n_upper+1)]
    
    print("\nGenerating sequences and storing path lengths...")
    path_len_list = [generate_collatz_sequence(n) for n in range_n]
    
    print("\nGenerating plot for path length multiplicities (frequencies)...")
    generate_plot_multiplicities(path_len_list)

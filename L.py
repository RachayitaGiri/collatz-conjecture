from collatz import generate_collatz_sequence

import matplotlib.pyplot as plt
import numpy as np

def generate_plot_path_lengths(range_n: list, path_len_list: list, batch_size: int = 10000):
    # Calculate the mean and standard deviation
    mean, std = np.mean(path_len_list), np.std(path_len_list)
    std_positive = mean + std
    std_negative = mean - std

    # Create a new figure for the full plot
    plt.figure(figsize=(15, 7))

    # Define the number of batches
    num_batches = len(range_n) // batch_size + (len(range_n) % batch_size > 0)

    # Plot each batch
    for i in range(num_batches):
        # Get the start and end indices for the current batch
        start_idx = i * batch_size
        end_idx = start_idx + batch_size

        # Ensure we don't go out of bounds
        end_idx = min(end_idx, len(range_n))

        # Plot the current batch
        plt.scatter(range_n[start_idx:end_idx], np.array(path_len_list)[start_idx:end_idx], c='blue', s=2)

    # Plot the mean, +1 standard deviation, and -1 standard deviation
    plt.axhline(y=mean, color='r', linestyle='-', label=f"Mean: {round(mean, 2)}")
    plt.axhline(y=std_positive, color='g', linestyle='dashed', label=f"+1 Std Dev: {round(std_positive, 2)}")
    plt.axhline(y=std_negative, color='g', linestyle='dashed', label=f"-1 Std Dev: {round(std_negative, 2)}")

    # Set properties of the plot
    plt.title(f"Collatz Path Lengths for Integers from {range_n[0]} - {range_n[-1]}")
    plt.xlabel("Integer n")
    plt.ylabel("Path Length")
    plt.grid()
    plt.legend()

    # Save the figure as a PNG
    plt.savefig('L.png')

    # Close the figure to release resources
    plt.close()

if __name__ == '__main__':
    n_lower = 1
    n_upper = 1000000
    range_n = [n for n in range(n_lower, n_upper+1)]
    
    print("\nGenerating sequences and storing path lengths...")
    path_len_list = [generate_collatz_sequence(n) for n in range_n]
    
    print("\nGenerating plot for path lengths...")
    generate_plot_path_lengths(range_n, path_len_list)

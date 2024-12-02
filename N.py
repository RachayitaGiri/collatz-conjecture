from collatz import generate_collatz_sequence_variant

import matplotlib.pyplot as plt
import numpy as np

def generate_plots(red_group: dict, blue_group: dict, batch_size: int = 10000):
    # Convert the group keys and values to numpy arrays for easy slicing
    blue_keys = np.array(list(blue_group.keys()))
    blue_values = np.array(list(blue_group.values()))
    
    red_keys = np.array(list(red_group.keys()))
    red_values = np.array(list(red_group.values()))

    # Create a new figure for the full plot
    plt.figure(figsize=(15, 7))

    # Define the number of batches
    num_batches_blue = len(blue_keys) // batch_size + (len(blue_keys) % batch_size > 0)
    num_batches_red = len(red_keys) // batch_size + (len(red_keys) % batch_size > 0)

    # Plot the blue group in batches
    for i in range(num_batches_blue):
        start_idx = i * batch_size
        end_idx = start_idx + batch_size
        end_idx = min(end_idx, len(blue_keys))

        # Plot the current batch of blue group
        plt.scatter(blue_keys[start_idx:end_idx], blue_values[start_idx:end_idx], c='blue', s=2)

    # Plot the red group in batches
    for i in range(num_batches_red):
        start_idx = i * batch_size
        end_idx = start_idx + batch_size
        end_idx = min(end_idx, len(red_keys))

        # Plot the current batch of red group
        plt.scatter(red_keys[start_idx:end_idx], red_values[start_idx:end_idx], c='red', s=2)

    # Plot dummy points for legend (one blue dot and one red dot)
    plt.scatter([], [], c='blue', s=10, label='Paths to 1')
    plt.scatter([], [], c='red', s=10, label='Paths that loop')

    # Set properties of the plot
    plt.title("Modified Collatz Path Length Distribution (3n-1)")
    plt.xlabel("Integer n")
    plt.ylabel("Path Length")
    plt.grid()
    plt.legend()

    # Save the figure as a PNG
    plt.savefig('N.png')

    # Close the figure to release resources
    plt.close()

if __name__ == '__main__':
    n_lower = 1
    n_upper = 1000000
    range_n = [n for n in range(n_lower, n_upper+1)]
    
    blue_group = {}
    red_group = {}

    print("\nGenerating sequences and storing path lengths...")
    for n in range(n_lower, n_upper+1):
        path_len, group = generate_collatz_sequence_variant(n)
        if (group == 'reaches 1'):
            blue_group[n] = path_len
        else:
            red_group[n] = path_len

    print("\nGenerating plot for path lengths for blue and red groups...")
    generate_plots(red_group, blue_group)

from collatz import generate_collatz_sequence_variant

import matplotlib.pyplot as plt
import numpy as np

def generate_plots(red_group: list, blue_group: list):
    # Plot the blue group as a scatter plot
    for n in range_n:
        plt.scatter(x=blue_group.keys(), y=blue_group.values(), c='blue', s=2)
    # Plot the red group as a scatter plot
    for n in range_n:
        plt.scatter(x=red_group.keys(), y=red_group.values(), c='red', s=2)

    # Set peoperties of the plot
    plt.title("Modified Collatz Path Length Distribution (3n-1)")
    plt.xlabel("Integer n")
    plt.ylabel("Path Length")
    plt.grid()
    plt.savefig('N-path-length-groups-plot.png')
    plt.close()

if __name__ == '__main__':
    n_lower = 1
    n_upper = 500
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

    generate_plots(red_group, blue_group)
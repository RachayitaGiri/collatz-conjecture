import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

def generate_plot_path_lengths(range_n: list, pathLenList: list):
    # Plot the path lengths as a scatter plot
    for n in tqdm(range_n):
        plt.scatter(n, pathLenList[n-1], c='blue', s=2)

    # Convert path length list to a numpy array
    pathLenArr = np.array(pathLenList)

    # Calculate the mean and standard deviation
    mean, std_positive = np.mean(pathLenArr), np.std(pathLenArr)
    delta = std_positive - mean
    std_negative = mean - delta

    # Plot the mean and standard deviation
    plt.axhline(y=mean, color='r', linestyle='-', label=f"Mean: {round(mean, 2)}")
    plt.axhline(y=std_positive, color='g', linestyle='dashed', label=f"+1 Std: {round(std_positive, 2)}")
    plt.axhline(y=std_negative, color='g', linestyle='dashed', label=f"-1 Std: {round(std_negative, 2)}")

    plt.title(f"Collatz Path Lengths for Integers from {range_n[0]} - {range_n[-1]}")
    plt.xlabel("Integer n")
    plt.ylabel("Path Length")
    plt.grid()
    plt.legend()
    plt.savefig('challenge1/ch1-path-length-plot.png')
    plt.close()

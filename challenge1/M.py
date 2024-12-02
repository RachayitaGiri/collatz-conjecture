import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
from collections import Counter

def generate_plot_multiplicities(range_n: list, pathLenList: list):
    # Calculate the path length frequencies and store as a dictionary --> n: freq(n)
    pathLenFreqs = Counter(pathLenList)

    # Plot the path length frequencies as a scatter plot
    for n in tqdm(range_n):
        plt.scatter(n, pathLenFreqs[n-1], c='red', s=2)

    # Convert path length frequency list to a numpy array
    pathLenFreqArr = np.array(list(pathLenFreqs.values()))

    # Calculate the mean and standard deviation
    mean, std_positive = np.mean(pathLenFreqArr), np.std(pathLenFreqArr)
    delta = std_positive - mean
    std_negative = mean - delta

    # Plot the mean and standard deviation
    plt.axvline(x=mean, color='b', linestyle='-', label=f"Mean: {round(mean, 2)}")
    plt.axvline(x=std_positive, color='g', linestyle='dashed', label=f"+1 Std: {round(std_positive, 2)}")
    plt.axvline(x=std_negative, color='g', linestyle='dashed', label=f"-1 Std: {round(std_negative, 2)}")

    plt.title(f"Multiplicity Distribution of Collatz Path Lengths (Scatter Plot)")
    plt.xlabel("Collatz Path Length")
    plt.ylabel("Multiplicity (Frequency)")
    plt.grid()
    plt.legend()
    plt.savefig('challenge1/ch1-path-length-freq-plot.png')
    plt.close()
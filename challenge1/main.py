from tqdm import tqdm
from L import generate_plot_path_lengths
from M import generate_plot_multiplicities

def generate_collatz_sequence_recursive(n: int, pathLen: int):
    """
        Recursive implementation
        -----------------------------
        Given any integer n, we generate a Collatz sequence (path), by applying three rules:
        1) if n is even, divide it by 2,
        2) if n is odd, multiply by 3 and add 1,
        3) if n = 1, STOP.

        @params:
            n: int - an integer n from where the sequence will be calculated
            pathLen: int - an integer for the path/sequence length
        @return:
            returns the next term of the sequence, and the new length
            returns -1 as the next term to indicate STOP
    """

    if (n==1):
        # print(f"{n}")
        # print(f"Path length: {pathLen}\n")
        pathLenList.append(pathLen)
        return -1, pathLen
    
    # print(f"{n} --> ", end='')
    pathLen += 1

    if (n%2==0):
        return generate_collatz_sequence(n//2, pathLen), pathLen # // returns an 'int' instead of 'float' on division
    else:
        return generate_collatz_sequence(3*n+1, pathLen), pathLen

def generate_collatz_sequence(n: int, pathLen: int):
    """
        Non-recursive implementation
        -----------------------------
        Given any integer n, we generate a Collatz sequence (path), by applying three rules:
        1) if n is even, divide it by 2,
        2) if n is odd, multiply by 3 and add 1,
        3) if n = 1, STOP.

        @params:
            n: int - an integer n from where the sequence will be calculated
            pathLen: int - an integer for the path/sequence length
        @return:
            returns the next term of the sequence, and the new length
            returns -1 as the next term to indicate STOP
    """
    pathLen=0
    while n != 1:
        # print(f"{n} --> ", end='')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pathLen += 1
    # print(f"{n}")
    # print(f"Path length: {pathLen}\n")
    return pathLen

if __name__ == '__main__':
    n_lower = 1
    n_upper = 1000000
    range_n = [n for n in range(n_lower, n_upper+1)]
    
    print("\nGenerating sequences and storing path lengths...")
    pathLenList = [generate_collatz_sequence(n, 0) for n in tqdm(range_n)]
    
    print("\nGenerating plot for path lengths...")
    generate_plot_path_lengths(range_n, pathLenList)

    print("\nGenerating plot for path length multiplicities (frequencies)...")
    generate_plot_multiplicities(range_n, pathLenList)
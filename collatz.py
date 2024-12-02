from random import random

def generate_collatz_sequence(n: int):
    """
        Non-recursive implementation
        -----------------------------
        Given any integer n, we generate a Collatz sequence (path), by applying three rules:
        1) if n is even, divide it by 2,
        2) if n is odd, multiply by 3 and add 1,
        3) if n = 1, STOP.

        @params:
            int: n - an integer n from where the sequence will be calculated
        @returns:
            int: path_len - the path length of the sequence generated from n
    """
    path_len = 0
    while (n != 1):
        if (n % 2 == 0):
            n = n // 2
        else:
            n = 3 * n + 1
        path_len += 1
    return path_len

def generate_collatz_sequence_variant(n: int):
    """
        Non-recursive implementation
        -----------------------------
        Given any integer n, we generate a modified Collatz sequence (path), by applying three rules:
        1) if n is even, divide it by 2,
        2) if n is odd, multiply by 3 and subtract 1,
        3) if n = 1 or n has been reached before, STOP.

        @params:
            int: n - an integer n from where the sequence will be calculated
        @return:
            int: path_len - the path length of the sequence generated from n
            string: 'loop' - if the sequence looped
                    'reaches 1' - if the sequence converged to 1
    """
    seen = set()
    path_len = 0
    while (n!=1 and n not in seen):
        seen.add(n)
        if (n % 2 == 0):
            n = n // 2
        else:
            n = n * 3 -1
        path_len += 1
    return path_len, 'loop' if n != 1 else 'reaches 1'

def generate_collatz_sequence_probabilistic(n: int, p: float=0.5):
    """
        Non-recursive implementation
        -----------------------------
        Given any integer n, we generate a probabilistic Collatz sequence (path), by applying three rules:
        1) if n is even, divide it by 2,
        2) if n is odd, n = 3n+1 with probability p and formula n = 3n-1 with the remaining probability 1-p
        3) if n = 1 or n has been reached before, STOP.

        @params:
            int: n - an integer n from where the sequence will be calculated
            float: p - a floating point probability for the application of rule 2
        @returns:
    """
    path_len = 0
    while (n!=1):
        if (n % 2 == 0):
            n = n // 2
        else:
            n = 3 * n + 1 if random() < p else 3 * n -1
        path_len += 1
    return path_len

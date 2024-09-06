#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """ Helper function to generate primes
        using Sieve of Eratosthenes
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        p = 2
        while p * p <= limit:
            if primes[p]:
                for i in range(p * p, limit + 1, p):
                    primes[i] = False
            p += 1
        prime_numbers = [p for p in range(2, limit + 1) if primes[p]]
        return prime_numbers

    """ Determine the maximum n value in nums to
        calculate all primes up to that point
    """
    max_n = max(nums)
    primes_up_to_max = sieve_of_eratosthenes(max_n)

    # Track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        remaining = list(range(1, n + 1))  # Remaining numbers in the set
        primes_in_round = [p for p in primes_up_to_max if p <= n]

        turn = 0  # so turn = 0 means Maria's turn, 1 means Ben's turn
        while primes_in_round:
            current_prime = primes_in_round[0]

            # Remove prime and its multiples
            remaining = [num for num in remaining if num % current_prime != 0]

            # Update primes left in the round
            primes_in_round = [p for p in primes_in_round if p in remaining]

            # Switch turns
            turn = 1 - turn

        # Whoever's turn it was that could not make a move loses
        if turn == 1:  # If it was Ben's turn, Maria won
            maria_wins += 1
        else:  # If it was Maria's turn, Ben won
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

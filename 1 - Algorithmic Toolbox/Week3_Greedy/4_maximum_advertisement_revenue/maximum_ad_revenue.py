# plovesee
# November 21, 2020
# Implimented the max_dot_product
# naive solution supplied

from itertools import permutations


def max_dot_product_naive(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


def max_dot_product(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    # first sort both sequences in reverse order
    firstSorted = sorted(first_sequence, reverse=True)
    secondSorted = sorted(second_sequence, reverse=True)

    # track the total product
    max_product = 0

    # iterate over the lenght of the sequences
    # get the product of the next two largest numbers
    # and add to the max_product
    for i in range(len(firstSorted)):
        max_product += (firstSorted[i] * secondSorted[i])

    return max_product
    
if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))

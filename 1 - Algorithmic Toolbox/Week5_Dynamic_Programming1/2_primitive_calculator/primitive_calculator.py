# Uses python3
import sys

def optimal_sequence(n):
    minOps = [0] * (n + 1)


    for i in range(2, n + 1):
        ops = [i/3, i/2, i - 1] # putting this here because i needs to be defined; may need to move for space
        minOps[i] = n + 10

        for op in ops:
            if op % 1 == 0:
                numOps = minOps[op] + 1
                if numOps < minOps[i]:
                    minOps[i] = numOps

    return minOps[n]








    #
    # sequence = []
    # while n >= 1:
    #     sequence.append(n)
    #     if n % 3 == 0:
    #         n = n // 3
    #     elif n % 2 == 0:
    #         n = n // 2
    #     else:
    #         n = n - 1
    # return reversed(sequence)

input = sys.stdin.read()
n = int(input)
assert 1 <= n <= 10**6
print(optimal_sequence(n))
# sequence = list(optimal_sequence(n))
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')

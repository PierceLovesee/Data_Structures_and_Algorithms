# Pierce Lovesee
import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def minMax(i, j):
    low = +float("inf")
    high = -float("inf")
    for k in range(i, j - 1):
        a = evalt(M[i][k], M[k+1][j], ops[k])
        b = evalt(M[i][k], m[k+1][j], ops[k])
        c = evalt(m[i][k], M[k+1][j], ops[k])
        d = evalt(m[i][k], m[k+1][j], ops[k])
        low = min(low, a, b, c, d)
        high = max(high, a, b, c, d)
    return(low, high)

def paren(values, n):

    for i in range(n + 1):
        m[i][i] = values[i]
        M[i][i] = values[i]
    for s in range(n + 1):
        for i in range(((n + 1) - s)):
            j = i + s
            m[i][j], M[i][j] = minMax(i, j)
    return M[0][n]



if __name__ == "__main__":
    data = list(map(str, sys.stdin.read().split()))
    n = int((len(data) - 1) / 2) # n is the number of operators
    m = [[0] * (n + 1) for _ in range(n + 1)]
    M = [[0] * (n + 1) for _ in range(n + 1)]
    assert 0 <= n <= 14  # assertion based on grader
    values = [0] * (n + 1) # creats a list for holding 'int' values
    for i in range(0, (n + 1)): # pulls out all numbers and puts in 'int' list
        values[i] = int(data[i * 2])
    ops = data[1:((2 * n) + 1):2] # pulls out all ops and puts in 'str' list

    print(paren(values, n)) # need to change "input()"

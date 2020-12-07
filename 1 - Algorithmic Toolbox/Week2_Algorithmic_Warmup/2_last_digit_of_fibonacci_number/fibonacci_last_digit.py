# Uses python3
import sys
#
# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % 10

## povesee
## November 9th, 2020
## Pretty much just like the last assignment but mob 10 the output
def FibLastFast(n):    
    assert (0 <= n <= 10 ** 7), "n is too large, try something smaller than 10E7"
    ## creates a list with the first 2 entries of 1 and 0
    Fib = [0,1]
    ## loops through to the index from the input, calculating each Fib Number
    for i in range(2, n+1):
        ## Calculates each fib number
        nextFib = (Fib[i -1] + Fib[i - 2]) % 10
        ## appends the calculated number to the list
        Fib.append(nextFib)
    ## returning the requested fib number
    return Fib[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(FibLastFast(n))

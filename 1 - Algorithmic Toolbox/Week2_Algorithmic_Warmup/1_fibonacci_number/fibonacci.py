# plovesee
## November 9th, 2020

## or
# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     return calc_fib(n - 1) + calc_fib(n - 2)


## fast fibinachi number algorithm
def FibFast(n):
    ## creates a list with the first 2 entries of 1 and 0
    Fib = [0,1]
    ## loops through to the index from the input, calculating each Fib Number
    for i in range(2, n+1):
        ## Calculates each fib number
        nextFib = Fib[i -1] + Fib[i - 2]
        ## appends the calculated number to the list
        Fib.append(nextFib)
    ## returning the requested fib number
    return Fib[n]

## ask user for input on which fib number they would like
n = int(input())
## show the requested fibinach number after computing
print(FibFast(n))

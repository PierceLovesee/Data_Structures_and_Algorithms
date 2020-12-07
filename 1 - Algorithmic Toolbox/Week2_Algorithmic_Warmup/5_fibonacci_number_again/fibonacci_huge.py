# plovesee
## November 13th, 2020
import sys


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    ## fast fibinachi number algorithm
    def FibFast(n):
        """
        Computes the nth Fibonacci number in near linear time O(n)
        as opposed to exponential time O(x^n) with recursive approach

        :param n: integer, the index of the Fibonacci number desired
        :return: int, the value of the Fibonacci number desired
        """
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


    ## 1.) find the pisano period
    ## this integer will be << Fn
    ## so we are able find it by direct computation
    def pisano_period(m):
        """
        Find the Pisano Period when the set of Fibonacci numbers is
        moded by m (i.e. Fn % m)

        :param m: integer, Fn % m
        :return: integer, Pisano Period
        """
        thisOne, nextOne = 0, 1
        for i in range(1, m*m*m):
            ## computing the list of Fn % m is the same as
            ## computing the list of Fn and then findin the % m
            ## of each entry, so to save space, just find the
            ## % m values
            thisOne, nextOne = nextOne, (thisOne + nextOne) % m

            ## check if 0, 1 has occured again, if so return the Pisano Period
            if (thisOne == 0 and nextOne == 1):
                return i

    ## 2.) find the remainder, k, when n % (pisano period)
    ## both k and n will be at the same index of the Pisanno Series
    ## so calculating Fn % m and Fk % m will yield the same result
    ## however, Fk << Fn, so Fk is much much easier to compute
    k = n % pisano_period(m)

    ## 3.) then find the kth fibonacci number, then returning Fk % m
    ## (i.e Fn % m == Fk % m)

    return FibFast(k) % m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(fibonacci_number_again(n, m))



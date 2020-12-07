# Uses python3
import sys



def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    ## creates a list with the first 2 entries of 1 and 0
    Total = 1
    Fib = [0, 1]
    ## loops through to the index from the input, calculating each Fib Number
    for i in range(2, n + 1):
        ## Calculates each fib number
        nextFib = (Fib[i - 1] + Fib[i - 2]) % 10
        ## appends the last digit of the calculated number to the list
        Fib.append(nextFib)
        ## add to the running total, then mod to keep at 1 digit
        Total = (Total + nextFib) % 10
    ## returning the requested fib number
    return Total

def last_digit_of_the_sum_of_fibonacci_numbers(n):

    ## starting off the Fibonacci series

    thisOne, nextOne = 0, 1


    # Base case
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:

        # Pisano Period for % 10 is 60
        rem = n % 60

        # Checking the remainder
        if(rem == 0):
            return 0

        # The loop will range from 2 to
        # two terms after the remainder
        for i in range(2, rem + 3):
            thisOne, nextOne = nextOne, (thisOne + nextOne) % 60

        return((nextOne - 1) % 10)



PISANO = 60  # 1


def solution(n):
    if n < 2:
        return n

    n %= 60

    thisOne, nextOne = 0, 1
    result = 1
    for i in range(n):
        thisOne, nextOne = nextOne, ((thisOne + nextOne) % 10)
        result = (result + nextOne) % 10

    return (result - 1)

if __name__ == '__main__':
    input_n = int(input())
    print(solution(input_n))


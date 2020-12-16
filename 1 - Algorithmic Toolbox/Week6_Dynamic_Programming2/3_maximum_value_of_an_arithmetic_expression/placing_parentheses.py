# Uses python3
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

def get_maximum_value(dataset):
    #write your code here
    return 0


if __name__ == "__main__":
    data = list(map(str, sys.stdin.read().split()))
    n = int((len(data) - 1) / 2) # n is the number of operators
    assert 0 <= n <= 14  # assertion based on grader
    values = [0] * (n + 1) # creats a list for holding 'int' values
    for i in range(0, (n + 1)): # pulls out all numbers and puts in 'int' list
        values[i] = int(data[i * 2])
    ops = data[1:((2 * n) + 1):2] # pulls out all ops and puts in 'str' list

    print(get_maximum_value(input())) # need to change "input()"

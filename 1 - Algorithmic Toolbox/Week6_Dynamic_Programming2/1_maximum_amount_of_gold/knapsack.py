#Pierce Lovesee
#December 12th, 2020
import sys

def optimal_weight(capacity, w):


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))

    # assertions based on grader constraints
    assert 1 <= W <= 10**4
    assert 1 <= n <= 300
    for i in w:
        assert 1 <= i <= 10**5

    print(optimal_weight(W, w))

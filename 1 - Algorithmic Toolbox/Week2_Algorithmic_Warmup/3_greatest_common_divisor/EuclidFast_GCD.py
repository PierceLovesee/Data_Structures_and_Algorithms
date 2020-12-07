##plovesee Novemver 2020
##GCD Algorithom running in O(log(n))

def EuclidFast(a, b):
    if b == 0:
        return a
    else:
        return EuclidFast(b, a % b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(EuclidFast(a, b))

## plovesee
## November 9th, 2020


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    def GCD(a, b):
        if b == 0:
            return a
        else:
            return GCD(b, a % b)

    return int(((a/GCD(a, b))*b))

if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))

# python3
#plovesee - November 7th, 2020


def max_pairwise_product(numbers):
    n = len(numbers)
    largest = max(numbers)
    numbers.remove(largest)
    sec_largest = max(numbers)
    return int(largest * sec_largest)


if __name__ == '__main__':
    input_n = float(input())
    input_numbers = [float(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

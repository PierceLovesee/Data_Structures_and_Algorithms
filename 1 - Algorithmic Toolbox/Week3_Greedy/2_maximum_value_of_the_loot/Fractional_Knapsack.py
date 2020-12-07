# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    
    # first combine weights (value) and values (keys) into a dictionary
    # then sort the disctionary by values (key)
    unsorted_dictionary = dict(zip(values, weights))
    # empty dictionary to hold entries after sorting
    sorted_dictionary = {}
    sorted_keys = sorted(unsroted_dictionary.keys(), reverse=True) #sorting in decending order
    for i in sorted_keys:
        sorted_dictionary[i] = unsorted_dictionary[i]
    print(sorted_dictionary)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

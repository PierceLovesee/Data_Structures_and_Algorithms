# plovesee
# December 3rd, 2020
# 3-partition quick sort for few unique elements

from random import randint


def partition3(array, left, right):
    pivot = array[left] #define pivot; first element of array per random_quick sort
    lessThan = left #keep track of how many elements are less than the pivot
    i = left #keep track of what elements in array you have already looked at
    greaterThan = right # defines the point in array where the greater than elements start

    while i <= greaterThan:  #iterate until the element you are looking at is already greater than
        if array[i] < pivot:  # if the element you are looking at is less than the pivot
            # then swap places with the element that is just after the last less than element
            array[lessThan], array[i] = array[i], array[lessThan]
            lessThan += 1 # then increase the number of less thans
            i += 1 # then move to next element
        elif array[i] > pivot: # if the element is greater than the pivot
            # then swap places with the element before the last greater than element
            array[i], array[greaterThan] = array[greaterThan], array[i]
            greaterThan -= 1 # then move to the left with the greater than list
            # we do not increment i on this one since we moved the element to the left
            # side of the pivot
        else: # if the element is equal to the pivot
            i += 1 # just move to looking at the next element
    return lessThan, greaterThan # lessThan will be the left most element equal to pivot
                                  # greaterThan will be the right most element equal to pivot



def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    lessThan, greaterThan = partition3(array, left, right)
    randomized_quick_sort(array, left, lessThan - 1)
    randomized_quick_sort(array, greaterThan + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

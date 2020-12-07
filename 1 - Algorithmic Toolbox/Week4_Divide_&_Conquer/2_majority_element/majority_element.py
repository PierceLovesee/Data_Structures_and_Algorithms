# plovesee; December 2020
# helper function to move all the majority elemts from one half present in the
# other half's others to that half's majority elements

def extraction(majority, others):
    """
    majority is from left half; others is from right half
    or visa versa
    helper function to move all the majorities from both
    halfs to the other if needed
    (i.e. if left half majority is 3, but the rest of the
    left half has 5 in it, and the majority of right half
    is 5, then the 5 from the left half will be moved to
    the right half)
    """
    remainder = []  # empty list to hold the left over others
    for i in others: # iterate through the others
        if majority[0] == i: # checking to see if any elements belong in other halfs majority
            majority.append(i) # adding it to the majorities if it does
        else:
            remainder.append(i) # otherwise, the element is added to the remainders
    return [majority, remainder]

def majority_element(arr, left, right):
    #base case for recursive function:
    if left + 1 == right:
        return [[arr[left]], []]


    #recursion to get to base case
    m = int(left + (right - left) / 2) # define the mid point
    leftHalf = majority_element(arr, left, m) # recursively call on left half
    rightHalf = majority_element(arr, m, right) #recurs. call on right half
    # essentially performing merge sort division tree
    # only difference is we are sorting to have the majority element present
    # first in the array after sorting

    # once base case is reached, start comparing left half and righ halfs
    # from the stack.  Take any left half majority elements present in the
    # right half non-majority elements, and place them in the left half
    # majority elements; do the same for the rirght half majority elements and
    # the left half non-majority elements
    [leftMajority, rightOthers] = extraction(leftHalf[0], rightHalf[1])
    [rightMajority, leftOthers] = extraction(rightHalf[0], leftHalf[1])

    #
    if leftMajority[0] == rightMajority[0]:
        return [leftMajority + rightMajority, leftOthers + rightOthers]
    elif len(leftMajority) > len(rightMajority):
        return [leftMajority, rightMajority + leftOthers + rightOthers]
    else:
        return [rightMajority, leftMajority + leftOthers + rightOthers]


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    assert len(input_elements) <= 10 ** 5
    mostCommon = majority_element(input_elements, 0, input_n)
    if len(mostCommon[0]) > (input_n / 2):
        print(1)
    else:
        print(0)

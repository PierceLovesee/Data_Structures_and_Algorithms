# python3
# Pierce Lovesee
# December 26th, 2020

from collections import namedtuple

# defining bracket data structure named tuple
Bracket = namedtuple("Bracket", ["char", "position"])

# helper function to determine if two sets of parens are matching
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = [] #stack to hold open parens
    # enumerate takes the sting and creates a list of lists, each elemnt is a
    # two element list that has the numbered location of each element in text
    # and the char at each element in text (i.e. [[0, p], [1, i], ... [5, e]])
    for i, next in enumerate(text):
        # case for handeling open parens
        if next in "([{":
            # creats new instance of Braket
            open = Bracket(next, i + 1)
            # pushes to stack
            opening_brackets_stack.append(open)
        # case for handeling close parens
        if next in ")]}":
            # if the stack is empty, then the current item is an issue
            if len(opening_brackets_stack) == 0:
                return(i + 1)
            # pop item from stack for comparison
            top = opening_brackets_stack.pop()
            # if the popped item and the current item do not match, then issue
            # at current item
            if not are_matching(top[0], next):
                return i + 1
    # Note: if a list is empty in Python3, then the bool value of the list
    # evaluates to False; if the list is not empty, bool value is True for list
    # If the above loop is completed and the stack is empty, then there are no`
    # mismatched parens
    if not bool(opening_brackets_stack):
        return "Success"

    # Otherwise, we know that at least the to of the stack is mismatched
    else:
        end = opening_brackets_stack.pop()
        return end.position

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()

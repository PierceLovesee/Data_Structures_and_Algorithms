# Uses python3
def edit_distance(s, t):
    """
       s: subject string to convert
       t: target string for conversion of s
       
       1 <= len(s or t) <= 100 
    """
    # grader assertions
    assert 1 <= len(s) <= 100
    assert 1 <= len(t) <= 100
    
    # create 2 dimm list (array) initiallizing with inf for easy comparison
    # indexing into table: T[row][column]
    # s is the subject string; t is the target string
    columns = len(t) + 1
    rows = len(s) + 1
    T = [[float("inf")] * columns for _ in range(rows)]
    
    # populate first colum with incrimental values starting at 0
    for i in range(rows):
        T[i][0] = i

    # populate first row with incrimental values starting at 0
    for j in range(columns):
        T[0][j] = j
        
    for row in range(1, rows):
        for column in range(1, columns):
            diff = 0 if s[row - 1] == t[column - 1] else 1 # accounts for (mis)match
            # selects the path of least effort based on previous decisions
            T[row][column] = min(T[row - 1][column] + 1,   # deleation
                            T[row][column - 1] + 1,        # insertion
                            T[row - 1][column - 1] + diff) # (mis)match

    return T[len(s)][len(t)]
    
if __name__ == "__main__":
    print(edit_distance(input(), input()))

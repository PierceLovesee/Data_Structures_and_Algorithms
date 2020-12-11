T = dict()

def ed(a, b, i, j):
    if not(i,j) in T:
        if i == 0: T[i,j] = j
        elif j == 0: T[i,j] = i
        else:
            diff = 0 if a[i-1] == b[j-1] else 1
            T[i,j] = min(
                ed(a, b, i-1, j) + 1,
                ed(a, b, i, j-1) + 1,
                ed(a, b, i-1, j-1) + diff)
    return(T[i, j])
print(ed(a="editing", b="distance", i = 7, j = 8))

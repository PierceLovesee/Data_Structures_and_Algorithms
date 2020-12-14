
# Logic
0th row has to be all True.  This represents that any valid sum of elements in ___A___ summing ___p___ can have 0 added to them and still be valid.

0th column has to be all Fasle, except for ___T[0][0]___ set to True, becuase otherwise the entire Truth table would evaluate to True.



The last row is treated differently than the rest of the matrix; it can not carry over the boolean value from the cell to it's left (or "skip" the element in A) because the last row shows what combinations work.  A True in T[p] indicates the existance on a valid combiniation of some elements in A that sum to be equal to ___sum(A) / 3____.  Then, if there are at least 3 True's in row ___p___ of the matrix, then is is possible to partition the array ___A___ into 3 equal parts. 

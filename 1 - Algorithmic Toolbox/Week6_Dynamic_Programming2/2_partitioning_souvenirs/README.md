
# Logic
0th row has to be all True.  This represents that any valid sum of elements in ___A___ summing ___p___ can have 0 added to them and still be valid.

0th column has to be all Fasle, except for ___T[0][0]___ set to True, becuase otherwise the entire Truth table would evaluate to True.



The last row is treated differently than the rest of the matrix; it can not carry over the boolean value from the cell to it's left (or "skip" the element in A) because the last row shows what combinations work.  A True in T[p] indicates the existance on a valid combiniation of some elements in A that sum to be equal to ___sum(A) / 3____.  Then, if there are at least 3 True's in row ___p___ of the matrix, then is is possible to partition the array ___A___ into 3 equal parts.



## Week 6 - Dynamic Programming 2
### Partitioning Souvenirs
#### Problem Introduction:
You and two of your friends have just returned back home after visiting various countries. Now you would like to evenly split all the souvenirs that all three of you bought.

#### Choice of Algorithm:
The solution to this problem is to first recognize that the will be a discrete non-repeating knapsack problem.  We know that we can not successfully implement a greedy algorithm to solve this problem, we need to use a dynamic programming approach.  The implementation will be similar to the gold knapsack problem previously implemented this week.

#### Implementation:
##### Inputs:
We will need to following inputs to solve this problem:

1. **n**: int; total number of souviners
2. **A**: list of ints; values of all souviners

User input will be in the form ___n, A<sub>0</sub>, A<sub>1</sub>, ... , A<sub>n - 1</sub>___ on one line in the prompt.

##### Outputs:
The prorgram will output _1_ if the elements in ___A___ are able to be evenly divided into 3 partitions; outputs _0_ otherwise.

##### Algorithm:
To solve this problem, we will need to create a two dimmensional array, or table ___T___, to act as a truth table.  The table will have ___n___ columns and ___p___ rows.  All elements of ___T___ will be initialized to ___False___, except for the first row, ___T[0]___, which will be initialized to _True_

To solve this problem, we will need to create a two dimensional array (2-dimensional list) to hold the maximum amount of gold we are able to hold at each incremental unit of knapsack capacity. This array, or table, will be constructed of ___n + 1___ columns and ___capacity + 1___ rows.

The fist column (representing no items taken) will be filled with zeros.

Then a 2 dimensional loop will be executed; looping though all incremental weights in ___capacity___ within a loop iterating through all items in ___w___. For each cell, the value will be initialized to the value immediately to it's left (assuming the subject item will be skipped, and then compared from there).

If the current row index (i.e. the incremental capacity of the knapsack) is greater than or equal to the weight of the subject item (i.e. ___w[column_index - 1]___), then it is possible to fit the subject item in the knapsack, so further comparison is needed; if not then the "item is skipped" and the incremental capacity of the knapsack is increased by one, and the comparison continues.

If the subject item can fit into the incremental capacity of the knapsack, then value stored in the table cell is the maximum of the following:
1. skipping the subject item
2. or, the weight of the subject item plus the value (weight) stored in the table in the column of the previous item and at the row of ___incremental_weight - weight_of_subject_item___ (essentially going back and checking if both this item, and the last item can fit)

Once this 2-dimensional loop has computed all possible combinations of incremental weights and combinations of items, the maximum amount of loot able to fit in the bag, while remaining less than or equal to the capacity of the knapsack will be stored if the cell corresponding to the last item in ___w___ and the full capacity of the knapsack ___capacity___ (i.e. Value[capacity][n]).

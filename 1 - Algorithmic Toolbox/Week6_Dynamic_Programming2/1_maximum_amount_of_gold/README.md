## Week 6 - Dynamic Programming 2
### Maximum Amount of gold
#### Problem Introduction:
You are given a set of bars of gold and your goal is to take as much gold as possible into
your bag. There is just one copy of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar).

#### Choice of Algorithm:
The solution to this problem is to first recognize that the will be a discrete non-repeating knapsack problem.  We know that we can not successfully implement a greedy algorithm to solve this problem, we need to use a dynamic programming approach.  

#### Implementation:
###### Inputs:
We will need to following inputs to solve this problem:
1. **capacity**: int; the total capacity of the knapsack
2. **n**: int; total number of bars of gold
3. **w**: list of ints; weights of _**n**_ bars of gold

___Note___: We will not need a list of values for each bar; each unit weight of the gold is assumed to be the same value.

###### Outputs:
The program will out put the maximum weight of gold we can fit in the bag based on the weights of the discrete bars of gold.

###### Algorithm:
To solve this problem, we will need to create a two dimensional array (2-dimensional list) to hold the maximum amount of gold we are able to hold at each incremental unit of knapsack capacity. This array, or table, will be constructed of ___n + 1___ columns and ___capacity + 1___ rows.  

The fist column (representing no items taken) will be filled with zeros.

Then a 2 dimensional loop will be executed; looping though all incremental weights in ___capacity___ within a loop iterating through all items in ___w___. For each cell, the value will be initialized to the value immediately to it's left (assuming the subject item will be skipped, and then compared from there).  

If the current row index (i.e. the incremental capacity of the knapsack) is greater than or equal to the weight of the subject item (i.e. ___w[column_index - 1]___), then it is possible to fit the subject item in the knapsack, so further comparison is needed; if not then the "item is skipped" and the incremental capacity of the knapsack is increased by one, and the comparison continues.

If the subject item can fit into the incremental capacity of the knapsack, then value stored in the table cell is the maximum of the following:
1. skipping the subject item
2. or, the weight of the subject item plus the value (weight) stored in the table in the column of the previous item and at the row of ___incremental_weight - weight_of_subject_item___ (essentially going back and checking if both this item, and the last item can fit)

Once this 2-dimensional loop has computed all possible combinations of incremental weights and combinations of items, the maximum amount of loot able to fit in the bag, while remaining less than or equal to the capacity of the knapsack will be stored if the cell corresponding to the last item in ___w___ and the full capacity of the knapsack ___capacity___ (i.e. Value[capacity][n]). 

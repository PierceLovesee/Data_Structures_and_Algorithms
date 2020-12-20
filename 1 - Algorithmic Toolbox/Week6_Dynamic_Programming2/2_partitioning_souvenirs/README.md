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
To solve this problem, we will need to create a two dimensional array, or table ___T___, to act as a truth table.  The table will have ___n___ columns and ___p___ rows.  All elements of ___T___ will be initialized to ___False___, except for the first row, ___T[0]___, which will be initialized to _True_

What the algorithm does is determines what combinations of the souvenirs result in valid combinations (i.e. value adds to be 1/3 of the total value of the souvenirs).  Each item is considered along all possible values of ___p___, if it can fit into ___p<sub>i</sub>___ then, and if ___i - value<sub>item</sub>___ in the same column is equal to ___True___ (i.e. meaning that there is a valid combination that will get you to that depth in the table) then the subject cell is set to True.  Was a point along ___p___ is found where an item is valid, that ___True___ value is carried right though out the table.  What this allows is for some items to be "skipped" in consideration for certain combinations (i.e. items 1, 4, 5 are a valid combination, but items 1, 2, 3, 4 is not a valid combination).  As the algorithm progresses from left to right in the table, it will begin to come to valid combinations that sum to ___p___.  Only the first ___p - 1___ rows are considered in the first part of the algorithm.  

Once all items have been considered, and all rows or possible combinations have been evaluated up to ___p - 1___ a second iterative algorithm is used to evaluate the last row.  The last row of the table represents if each respective item has a valid combination to sums to ___p___.  This part of the code uses a separate loop because we do not want to carry over the value from the previous column in the row like we have to do in the rest of the table (to be able to skip items).  Considering each item, the algorithm looks at the value in ___row = p - value<sub>item</sub>___ and ___column = column<sub>item</sub> - 1___; if this value is ___True___ then there is a valid combination with the subject item as the last element, so ___True___ is recorded in the last row under the item, otherwise that value remains ___False___.  Each item is considered in this way.

Once the last row of the table is resolved, each ___True___ in the last row is counted.  If there more than three ___Trues___, then we know that there are at least three valid combinations of the souvenirs that sum to a value of exactly ___p___; meaning the souvenirs are indeed able to be evenly partitioned into three equal parts.

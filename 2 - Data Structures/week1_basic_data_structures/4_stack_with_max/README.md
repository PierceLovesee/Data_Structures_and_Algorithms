## Extending Stack Interface to Return Max Value of Stack

### Problem Introduction:
Stack is an abstract data type supporting the operations Push() and Pop(). It is not difficult to implementit in a way that both these operations work in constant time. In this problem, your goal will be to implement a stack that also supports finding the maximum value and to ensure that all operations still work in constant time.

### Problem Description:
We will need to find a way to extend the stack interface to include the use a function **Max** that will return the maximum value currecntly in the stack; this function must also run in contant time (***O(1)***) like **Pop** and **Push**.  The crux of this problem is to recognize the following:

  - for a stack of size ***n*** elements the following must be true
    - there must be a maximum value in the stack
    - and, if the max value of the stack does not occure in the range ***i to (n-1)***, then all elements in that same sub-set range have the same maximum value

What this allows us do is keep an auxilirary stack that maintains the current max of the stack where the last element of the auxilirary stack will always be the maximum of the main stack, and therefore, the max of the stack will be able to be accessed in constant time.

### Inputs / Outputs:
First prompt line will be ***n***, the number of queries you plan to make on the stack (pushes, pops, calls to max).  Subsequent input will be calls to the stack.  The following are supported in the interface:

- **pop** - removes the top (last) element of the stack; nothing will print
- **push (int)** - appends the user input ***(int)*** value to the top (last element) of the stack; nothing will print
- **max** - prints the maximum value currently on the stack
- **print** - prints the current stack in a list format; bottom element on left, top element on right

### Implementation:
As mentioned above, the crux of this problem is to recognize two things:
- for any given stack of size ***n*** elements, there must be a maximum value
- and, if the max value of the stack does not occure in the range ***i to (n-1)***, then all elements in that same sub-set range of ***i to (n-1)*** must have the same maximum Value

Recognizing this allows us to only maintain the current max of the stack on the auxilirary stack and not be concerned with the non-maximum values of the stack.  This allows us to completely avoid the need to sort of search the auxilirary stack in any way.  A naive solution to this problem would consist of us keeping track of all elements of the main stack and then sorting the auxilirary stack as needed when new elements are pushed to the stack and then searching the auxilirary stack and removing items as items are popped from the stack.  However, this solution would run in ***O(nlogn)*** time at best and would not be optimal.

In order to implement a solution that returns the Max value in constant time, the auxilirary stack will have the same number of elements as the main stack, but for each new element pushed to the stack, the following comparisons will be made:
- if the auxilirary stack is empty, or if the last element of the auxilirary stack (i.e. the current max of the stack) is less than the new element pushed to the stack, then the new element is also pushed to the auxilirary stacks
-  if the new element being pushed to the stack is less than the current max (i.e. the last element of the auxilirary stack) then a redundent copy of the last element of the auxiliary stack is pushed to the end of the auxilirary stack.
    - **i.e.** if a new max is found being pushed to the stack, then that max is pushed to the auxiliary stack.  Then if say 5 more elements are pushed to the stack, but none of them are new maximum values, then there will be 6 of same maximum elements in a row on the auxilirary stack, representing that for those six elements on the stack, the same max value exists

Now that we have the ability to push elements to the stack and keep track of the current maximum for each element, we now need to be able to pop items from the stack and track the maximum with those changes as well.  The solution to this is relatively trivial in implementation; we simply need to pop an item from the main stack as well as pop an item from the auxilirary stack.  Since the maximum value on the stack for each element is tracked in the auxilirary stack, as we pop items from both stacks, the maximum value of the stack will always be help at the top of the auxilirary stack.

Knowing that the maximum value of the stack will always be held at the top of the auxilirary stack allows us to access the max in constant time.  To return the max of the stack, we simply return the value at the [-1] index of the auxilirary stack, which runs in ***O(1)*** time.  

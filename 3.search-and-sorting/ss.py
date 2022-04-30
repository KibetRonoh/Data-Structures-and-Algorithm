"""

Searches and sorts can be very hard to visualize and understand. If you need, go through the video a few more times until it really sinks in. Here is a supplementary visualization that might help as well!

Python lists have a method called index(), which just does a search and returns the first index with an instance of that value. Next, you're going to write a binary search function that has the same result, but searches faster. Keep in mind the constraint for this exercise—for binary search, elements need to be in increasing order.


"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)







We're going to take a look at recursion with a famous example—the Fibonacci Sequence.

The Fibonacci Sequence follows one rule: get the next number in the sequence by adding the two previous numbers. Here is an example of the sequence:

0,1,1,2,3,5,8,13,21,34...
Step through each value. You start with 0 and 1. 0 + 1 = 1, so you add 1 to the sequence. 1 + 1 = 2, so 2 is added. 1 + 2 = 3, so 3. 2 + 3 = 5, et cetera.

You could represent these numbers as Python list, and it would look something like this:

fib_seq = []
fib_seq[0] = 0
fib_seq[1] = 1
fib_seq[2] = 1
fib_seq[3] = 2
fib_seq[4] = 3
fib_seq[5] = 5
fib_seq[6] = 8
fib_seq[7] = 13
fib_seq[8] = 21
fib_seq[9] = 34
We can generate this sequence using an iterative method (with loops):

function getFib(position) {
  if (position == 0) { return 0; }
  if (position == 1) { return 1; }
  var first = 0,
      second = 1,
      next = first + second;
  for (var i = 2; i < position; i++) {
    first = second;
    second = next;
    next = first + second;
  }
  return next;
}
In the quiz, you'll be implementing get_fib() in a recursive way.










####################################
"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    return -1

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)








####################
Sorting techniques can be tricky—sometimes the best way to understand them is to watch a visual of a sorting algorithm in action again and again. When I was first learning sorting, I used to check out the Wikipedia page for each sort. There's normally some colorful illustration near the top, then a GIF showing the sort in action. There are plenty of other visualizations on the World Wide Web—take the time to look around if you need it!


#################

Sorting is pretty tedious—take a break and check out this comic inspired by merge sort.

You can learn more about merge sort, as well as see many more visualizations, in the online Algorithms textbook. This book is often nice for a more in-depth analysis of topics, but beware—all of the examples are in Java! For merge sort, it's particularly worth reading up on top-down and bottom-up merge sort.


############
"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    return []

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)




"""
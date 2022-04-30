"""
Collections in Python are containers used for storing data and are commonly known as data structures, such as lists, tuples, arrays, dictionaries, etc.

Python has a built-in collections module providing additional data structures for collections of data.




Python has an interesting data stucture called a "list" that is much more than a mere list. In fact, a Python list actually encompasses the functionality of almost every list-based data structure in this lesson.

Behind the scenes a Python list is built as an array. Even though you can do many operations on a Python list with just one line of code, there's a lot of code built in to the Python language running to make that operation possible.

For example, inserting into a list is easy (happens in constant time). However, inserting into an array is O(n), since you may need to shift elements to make space for the one you're inserting, or even copy everything to a new array if you run out of space. Thus, inserting into a Python list is actually O(n), while operations that search for an element at a particular spot are O(1). You can see the runtime of other list operations here.

Python is a "higher level" programming language, so you can accomplish a task with little code. However, there's a lot of code built into the infrastructure in this way that causes your code to actually run much more slowly than you'd think. Keep this in the back of your mind when using Python. You likely won't need to know the details of how Python works behind the scenes in a programming interview, but you'll seem very impressive if you do!

If you aren't already comfortable with Python lists, you can look through this lesson about basic Python list manipulation.




There isn't a built-in data structure in Python that looks like a linked list. Thankfully, it's easy to make classes that represent data structures in Python!

Here's the code for an Element, which will be a single unit in a linked list:

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
Make sure you understand this code before moving on! We use __init__ to initialize a new Element. An Element has some value associated with it (which could be anything—a number, a string, a character, et cetera), and it has a variable that points to the next element in the linked list.

Now, let's set up a LinkedList class:

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
This code is very similar—we're just establishing that a LinkedList is something that has a head Element, which is the first element in the list. If we establish a new LinkedList without a head, it will default to None.

Great! Let's add a method to our LinkedList to make it a little more useful. This method will add a new Element to the end of our LinkedList.

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
Again, this part is really important, so don't rush through it. Take the code line-by-line 
and make sure everything makes sense. If the LinkedList already has a head, iterate through 
the next reference in every Element until you reach the end of the list. Set next for the end 
of the list to be the new_element. Alternatively,
 if there is no head already, you should just assign new_element to it and do nothing else.




 Remember that wonderful Python list we talked about eariler? It turns out that stack functionality is already built into it!

The Python documentation shows how you can use built-in funtions to turn your Python list into a stack. pop() is a given function, and append() is equivalent to a push function.

Of course, this functionality makes stack manipulation in Python all too easy. Let's make our own Stack class to see how a stack really works under the hood.


Let's look at implementing queues in Python. Queue's are mentioned in Python's documentation. Examine the code below:

from collections import deque
From a library called collections, you can import a package called deque. As was mentioned in the video, a deque is a double-ended queue. You can enqueue on either end, but in the example you only enqueue one way and treat it as a normal queue.


"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        pass

    def peek(self):
        pass 

    def dequeue(self):
        pass
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()







"""

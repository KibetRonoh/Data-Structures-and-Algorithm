# Efficiency/Complexity
# How well you are using your computers resources to get the job done
# Get the most done with minimal resources
## Common data structures and the efficiency of doing basic things with them
###ALGORITHM - series of steps of solving a problem
# Time efficiency and space efficiency
# We Can define efficiency of code using Big O Notation O(n)
"""
-Pseudocode - is an informal way of programming description that does not 
 require any strict prog lang syntax
 - its used for creating an outline or rough draft of a program
 """

"""
################
O(n) - its a way to measure an algorithms efficiency. It measures the 
time it takes to run your function as the input grows
*Big O is sometimes refered to as algorithms upper bound, meaning it 
deals with the worst-case scenario
*\\

There are two parts of measuring efficiency:
1. Time complexity is a measure of how lomg the function takes to run in 
   terms of its computational steps
2. Space complexity has to do with the amount of memory used by the function

- WORST CASE scenarion
   * Checking all posible outcomes e.g checking the letters of 
   alphabet 26 times 
   * we focus on Worst case because it puts an upper bound to 
   ammount of time our code is going to take
   
       A B C D E .........M N ...........W X Y Z 
       1 2 3 ..........   13 .............24 25 26
       -1 is the best case
       -13 is Average case
       -26 is worst case
################



input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)
"""





def example2(manatees):
    print(manatees[0]['name'])
    print(manatees[0]['age'])


def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print(manatee_property, ": ", manatee[manatee_property])


def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print(oldest_manatee)

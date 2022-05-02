"""list = ['A',' B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
sliced_list = list[3:8]
sliced_list2 = list[5:]
sliced_list3 = list[:]
sliced_list4 = list[:-6]# from [0] to -6 excluding -6
sliced_list5 = list[-6:-1]
sliced_list6 = list[::-1]

print(sliced_list)
print(sliced_list2)
print(sliced_list3)
print(sliced_list4)
print(sliced_list5)
print(sliced_list6)

"""

lst =list(range(1, 11))
print (lst)

#  below list has numbers from 2 to 5
lst1_5 = lst[1 : 5]
print (lst1_5)

#  below list has numbers from 6 to 8
lst5_8 = lst[5 : 8]
print (lst5_8)

#  below list has numbers from 2 to 10
lst1_ = lst[1 : ]
print (lst1_)

#  below list has numbers from 1 to 5
lst_5 = lst[: 5]
print (lst_5)

#  below list has numbers from 2 to 8 in step 2
lst1_8_2 = lst[1 : 8 : 2]
print (lst1_8_2)

#  below list has numbers from 10 to 1
lst_rev = lst[ : : -1]
print (lst_rev)

#  below list has numbers from 10 to 6 in step 2
lst_rev_9_5_2 = lst[9 : 4 : -2]
print (lst_rev_9_5_2)

listest = lst[9 : 2 : -2]
print(listest)


"""
We can use the filter function to filter a list based on some 
condition provided as a lambda expression as 
the first argument and list as the second argument, 
an example of which is shown below :
"""
import functools

# filtering odd numbers
lst = filter(lambda x : x % 2 == 1, range(1, 20))
print (list(lst))
	
# filtering odd square which are divisible by 5
lst = filter(lambda x : x % 5 == 0,
	[x ** 2 for x in range(1, 11) if x % 2 == 1])
print (list(lst))
	
# filtering negative numbers
lst = filter((lambda x: x < 0), range(-5,5))
print (list(lst))
	
# implementing max() function, using
print (functools.reduce(lambda a,b: a if (a > b) else b, [7, 12, 45, 100, 15]))



# Python program to merge and sort two list
def Merge(list1, list2):
	final_list = list1 + list2
	final_list.sort()
	return(final_list)

# Driver Code
list1 = [25, 18, 9, 41, 26, 31]
list2 = [25, 45, 3, 32, 15, 20]
print(Merge(list1, list2))

##################################

def Merge(list1, list2):
	f_list = list1 + list2
	f_list.sort()
	return (f_list)

list1 = [6, 5, 4, 3, 2, 1, 0]
list2 = [6, 7, 8, 9]
print(Merge(list1, list2))
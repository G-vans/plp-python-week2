my_list = []

#append
my_list.extend([10,20,30,40])

#insert 15 at the second position
my_list.insert(1, 15)

#extend my list with another list
my_list.extend([50,60,70])

#remove the last element from my_list
my_list.pop()

#sort in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30 in my_list:", index_of_30)

# List (duplicates are allowed)
# mixture of items like int, string and boolean can be together in a list

my_list = [1,2,3,4]
my_list2 = [1,2,"Abhi",34,5,True]

# Indexing
print([my_list[0]])

# Changin the element
my_list[2]=30
print(my_list)

# Append(to add element)
my_list.append(56)
print(my_list)

#extend() the items of list
my_list.extend([45,67])
print(my_list)

# insert() in a list
my_list.insert(2,333)
print(my_list)

#remove() from list
my_list2.remove("Abhi")
print(my_list2)

#copy() the list
my_copy_list = my_list.copy()
print(my_copy_list)

#   Clear() the list
my_copy_list.clear()
print (my_copy_list)

# sort() the list
my_list.sort()
print(my_list)

# reverse() the list
my_list.reverse()
print(my_list)

# print each element
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

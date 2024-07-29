# unpacking of tuples
a, b, c = (23,45,67)

t=(23,45,67)
new_t= t+(54,)
print(new_t)

# OR By converting into list and append then convert into tuples again
my_list = list(t)
print(my_list)
my_list.append(55)
new_tuple2=tuple(my_list)
print(new_tuple2)
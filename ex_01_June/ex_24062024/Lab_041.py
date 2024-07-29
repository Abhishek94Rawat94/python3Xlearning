# Filters in python

# Built-in function in python filter() which allowed to filter the elements in a list,tuple and set

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# --> Filter the even numbers

def is_even(num):
    return num % 2 == 0


def is_greater_5(num):
    return num > 5


new_greater_numbers = filter(is_greater_5, numbers)
print(list(new_greater_numbers))

new_even_numbers = filter(is_even, numbers)
print(list(new_even_numbers))

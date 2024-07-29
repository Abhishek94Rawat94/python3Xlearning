# To iterate a dictionar

my_dict = {
    'b': 2,
    'a': 1,
    'c': 3
}

# To find a key

for k,v in my_dict.items():
    if k=='b':
        print("Key with the name b is found")

        # OR

op='b' in my_dict
print(op)
# List - Shopping List
# milk, butter, tea , coffee, sugar
# Add item
# Remove item
# Update item
# View item
# Exit
shopping_list = ["milk", "butter", "tea", "coffee", "sugar"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[3])
print(shopping_list[-2])

shopping_list.append("Banana") # Add item in list
print(shopping_list)

shopping_list.insert(2, "ice cream") # Insert in the middle
print(shopping_list)

shopping_list.extend(["chips", "salt"]) # Add multiple item in the end of list
print(shopping_list)

shopping_list.remove("Banana") # To remove item
print(shopping_list.pop())
print(shopping_list.index("butter")) # To find index

shopping_list.reverse()
# To reverse list
print(shopping_list)

shopping_list[0] = "Abhi"
shopping_list.sort() # To sorting the list
print(shopping_list)

my_list = [1, 2, 3, 4, True, 3.14, "Abhi"]
print(type(my_list))



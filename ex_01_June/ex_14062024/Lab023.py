# Multiple Condition
# Match Case
numbers = int(input("Enter the number"))
match numbers:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case _:
        print("Out of scope")

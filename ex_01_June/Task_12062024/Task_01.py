# A leap year is divisible by 4, but not by 100 unless it is also
# divisible by 400, Use an if-else statement to make this determination.

y = int(input("Enter the Year"))
if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
    print(f' {y} is a leap year.')
else:
    print(f'{y} is not a leap year')

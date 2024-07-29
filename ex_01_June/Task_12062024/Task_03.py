# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

a = int(input("Enter the number"))
fact = 1
for i in range(1, a+1):
    fact = fact*i
    print(f"Factorial of {a} is :", end=" ")
    print(fact)
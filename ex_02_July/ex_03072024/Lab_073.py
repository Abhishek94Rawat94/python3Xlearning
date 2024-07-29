# Exception handling

try:
    a = int(input("Enter the num1"))
    b= int(input("Enter the num2"))
    c=a/b
    print("result div is",c)
except Exception as e:
    print (e)
    print("Enter a valid digit")
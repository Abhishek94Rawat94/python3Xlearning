# Lambda expression : to do the task in a single line

def double_my_salary(salary):
    return salary*2

new_salary = double_my_salary(1000)
print (new_salary)

# by using lambda
f_double_salary = lambda salary:salary*2
print(f_double_salary(2000))
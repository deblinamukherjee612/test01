# python program to create a simple calculator

# 3 steps   to build a calculator program

# 1. functions for operations

# 2. user input

# 3. print result

# 1. functions for operations
# function to add 2 numbers
def add(x,y):
    return x+y

# function to subtract 2 numbers
def subtract(x,y):
    return x-y

# function to multiply 2 numbers
def multiply(x,y):
    return x*y

# function to divide 2 numbers
def divide(x,y):
    return x/y

# function to get average of 2 numbers
def avg(x,y):
    return(x+y)/2

# 2. user input

print("Select an operation from the following list \n" \
    " 1. Addition \n" \
    " 2. Subtraction \n" \
    " 3. Multiplication \n" \
    " 4. Division \n" \
    " 5. Average")

select = int(input("Select an operation from 1,2,3,4 and 5 : "))

num1= int(input("Enter the first number : "))

if select==4:
    num2= int(input("Enter the second number. Remember division by 0 is not possible." \
    "Please don't enter 0 in case of division. : "))
else:
    num2 = int(input("Enter the second number: "))

# 3. print result

if select == 1:
    print("sum of", num1, "and", num2, "is",\
          add(num1, num2))
elif select == 2:
    print("difference of", num1, "and", num2, "is",\
          subtract(num1, num2))
elif select == 3:
    print("product of", num1, "and", num2, "is",\
          multiply(num1, num2))
elif select == 4:
    print("division of", num1, "and", num2, "is",\
          divide(num1, num2))
elif select == 5:
    print("avg of", num1, "and", num2, "is",\
          avg(num1, num2))
else:
    print("Invalid input. Please enter a number from 1-5")

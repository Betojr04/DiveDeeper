"""'
TASK 1

Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

"""

print("Please enter 3 numbers.")

user_numbers = (
    input("Enter your first number"),
    input("Enter your second number"),
    input("enter your third number"),
)

if user_numbers[0] > user_numbers[1] and user_numbers[0] > user_numbers[2]:
    print(user_numbers[0])
elif user_numbers[1] > user_numbers[0] and user_numbers[1] > user_numbers[2]:
    print(user_numbers[1])
elif user_numbers[2] > user_numbers[1] and user_numbers[2] > user_numbers[0]:
    print(user_numbers[2])

"""
TASK 2

Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

"""

print("Please enter 3 numbers.")

user_numbers = (
    input("Enter your first number"),
    input("Enter your second number"),
    input("enter your third number"),
)
print(max(user_numbers))

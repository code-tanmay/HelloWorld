print('hello, world!')

# make a funcion that adds two numbers
def add_numbers(a, b):
    return a + b

# call add_numbers with two numbers and print the result
result = add_numbers(5, 3)
print('The sum of 5 and 3 is:', result)
# ask user for two numbers and print the result
user_input_a = int(input('Enter the first number: '))
user_input_b = int(input('Enter the second number: '))
user_result = add_numbers(user_input_a, user_input_b)
print(f'The sum of {user_input_a} and {user_input_b} is: {user_result}')
# This code prints a greeting and defines a function to add two numbers.
# It then calls the function with hardcoded values and user input.
# The result is printed to the console.
# The code is a simple Python script that demonstrates basic function usage and user input handling.

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Initializing variables - establishing their type'''

# integers are whole numbers
variable_integer = 1

## float is a number with a decimal. If you divide two integers Python will
## return a float even if the answer is a whole number
variable_float = 1.0

# a "string" is an "ordered set of characters"; you can think of it as text that
# can include any symbol
variable_string = "Hello"

# A boolean variable can only equal True or False
variable_boolean = False

# A list holds an ordered set of values. They can be any other type of variable
variable_list = [1,1.0,"Hello",False]
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Manipulating number variables: reassigning a variable

Here we ask the user for a number, assign our integer variable to be that
number, then print out a string including that number'''

print("\nREASSIGNING VARIABLES\n")

# Ask the user for a number
new_number = input("Give me a number: ")

# Set our integer variable to be that number
variable_integer = new_number

# Print a concatenated string - that means two strings put together.
# variable_integer is an integer, not a string, so we have to tell Python to
# change its format by using str() to turn it into a string
print("Your number is " + str(variable_integer))
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Manipulating number variables: Integers and Floats'''

print("\n\nINTEGERS AND FLOATS")

# Ask the user for a number
new_number = float(input("\nGive me a number: "))

# Show it in both integer and float value:
print("The integer value of your number is " + str(int(new_number)) +
      "\nand the float value of your number is " + str(new_number))
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Manipulating number variables: Operations'''

print("\n\nOPERATIONS")

# Ask the user for two numbers
first_number = int(input("\nGive me your first number: "))
second_number = int(input("\nGive me your second number: "))

# Show the sum
print("\nThe sum is " + str(first_number + second_number))

# Show the difference. abs() means absolute value
print("\nThe difference is " + str(abs(first_number-second_number)))

# Show the product
print("\nThe product is " + str(first_number * second_number))

# Show the quotient
print("\nThe quotient is " + str(first_number/second_number))

# Show the remainder when dividing
print("\nThe quotient is " + str(int(first_number/second_number)) + " and the "
      "remainder is " + str(first_number % second_number))
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


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
Manipulating strings variables: concatenating

Concatenating strings means putting together multiple strings'''

print("\nCONCATENATING STRINGS")

# Ask user for a word
word = input("Give me a word: ")

# Concatenate their answer to a set phrase
print("Your word is " + word)
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Manipulating strings variables: Picking out letters'''

# Ask the user for a word
word = input("Give me a word: ")

# Print the word letter by letter
# len(...) gets the length of your string
for i in range(len(word)):
    print(word[i])

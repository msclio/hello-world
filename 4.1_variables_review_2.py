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
Manipulating strings: Concatenating

Concatenating strings means putting together multiple strings'''

print("\nCONCATENATING STRINGS")

# Ask user for a word
word = input("Give me a word: ")

# Concatenate their answer to a set phrase
print("Your word is " + word)
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Manipulating strings: Picking out characters'''

print("\nPICKING CHARACTERS")

# Ask the user for a word
word = input("Give me a word: ")

# Print the word letter by letter (character by character)
# len(...) gets the length of your string
for i in range(len(word)):
    print(word[i])
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Manipulating strings: Scrambling letters

There is a theory that as long as the first and last letters are in the right
place, people can read the word even if the middle letters are scrambled'''

print("\nSCRAMBLING LETTERS")

# Ask the user for a long word
word = input("Give me a 5+ letter word: ")

# Scramble the word
middle_scramble = ""
for i in range(1,len(word)-1):
    middle_scramble = word[i] + middle_scramble
scrambled = (word[0] + middle_scramble + word[len(word)-1])
print(scrambled)
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Manipulating boolean variables: Long or short'''

print("\nLONG OR SHORT")

# Ask the user for a word
word = input("Give me a word: ")

# Create a boolean variable called "is_long" that is True if the word is longer
# than four letters
is_long = (len(word) > 4)

# Tell the user if their word is long or not based on the value of is_long
print("is_long is " + str(is_long))
if is_long:
    print("Your word is long")
else:
    print("Your word is short")




name = input("What's your name? ") # name saves the user's input

print("Hello "+name+"!") # concatenate words (add them to form a sentence)

print("Introduction to your game")

repeat = True


choice = input("What do you want to do?"
               "\na) do something"
               "\nb) do something else"
               "\nc) do a third thing"
               "\n\n") # "\n" creates a new line, so the user's input gets
                       # types below the options

if choice == "a": # checks whether the user's input is the letter "a"
    print("do something")
    
elif choice == "b": # "elif" is short for "else if"
    print("do something else")

elif choice == "c":
    print("do a third thing")

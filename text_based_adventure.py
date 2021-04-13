import random
import time


money_global = [0,0,0,0]
broom_global = 0
pet_global = 0
wand_global = ["","",""]
supply_list_global = [["The Standard Book of Spells, Grade 1 by Miranda Goshawk",0],
                      ["A History of Magic by Bathilda Bagshot",0],
                      ["A Beginner's Guide to Transfiguration by Emeric Switch",0],
                      ["One Thousand Magical Herbs and Fungi by Phyllida Spore",0],
                      ["Magical Drafts and Potions by Arsenius Jigger",0],
                      ["Fantastic Beasts and Where to Find Them by Newt Scamander",0],
                      ["1 Wand",0],
                      ["1 Cauldron",0]]



def main(money,wand,broom, pet, supply_list):
    intro(money,wand,broom,pet,supply_list)

def intro(money,wand,broom,pet,supply_list):

    print("            _            _.,----,")
    print(" __  _.-._ / '-.        -  ,._  \) ")
    print("|  `-)_   '-.   \       / < _ )/\" }")
    print("/__    '-.   \   '-, ___(c-(6)=(6)")
    print(",  `'.    `._ '.  _,'   >\    \"  )")
    print(" :;;,,'-._   '---' (  ( \"/`. -='/")
    print(";:;;:;;,  '..__    ,`-.`)'- '--'")
    print(";';:;;;;;'-._ /'._|   Y/   _/' \\")
    print("      '''\"._ F    |  _/ _.'._   `\\")
    print("             L    \   \/     '._  \\")
    print("      .-,-,_ |     `.  `'---,  \_ _|")
    print("      //    'L    /  \,   (\"--',=`)7")
    print("     | `._       : _,  \  /'`-._L,_'-._")
    print("     '--' '-.\__/ _L   .`'         './/")
    print("                 [ (  /")
    print("                  ) `{")
    print("                  \__)")

    print("Dear Mr. Potter,"
    "\n\nWe are pleased to inform you that you have been accepted at Hogwarts "
    "\nSchool of Witchcraft and Wizardry. Please find enclosed a list of all "
    "\nnecessary books and equipment."
    "\n\nTerm begins on 1 September. We await your owl by no later than 31 July."
    "\n\n\nYours sincerely,\n\nAlbus Dumbledore \nHeadmaster of Hogwarts")

    time.sleep(4)

    print("\n\nCongratulations on your acceptance to Hogwarts!")

    time.sleep(2)

    choice = input("\n\nWhat would you like to do?"
          "\na) Stay at the Dursleys'"
          "\nb) Send your owl immediately\n\n")

    time.sleep(0.5)

    if choice == "a":
        print("\n\nYou stay with the Dursleys until your 18th birthday"
              "\nand you live out a Muggle life"
              "\n\nThe End")
    elif choice == "b":
        print("\n\nGood choice. First stop: Diagon Alley. \nLet's go!")
        diagon_alley(money,wand,broom,pet,supply_list)
    else:
        print("That is not a valid answer")

def diagon_alley(money,wand,broom,pet,supply_list):

    move()

    print("\n\nWelcome to Diagon Alley")
    repeat = True

    while repeat == True:

        choice = input("\n\nYou see the following buildings."
                       "\nWhere would you like to go?\n"
                       "\na) Quality Quidditch Supplies"
                       "\nb) Potage's Cauldron Shop"
                       "\nc) Eeylops Owl Emporium"
                       "\nd) Flourish & Blott's"
                       "\ne) Florean Fortescue's Ice Cream Parlor"
                       "\nf) Gringotts Wizarding Bank"
                       "\ng) Ollivander's"
                       "\n\nOR\n"
                       "\nh) Check list"
                       "\ni) Leave Diagon Alley\n\n")


        if choice == "a":
            move()
            money,broom = quidditch_supplies(money,broom)
        elif choice == "b":
            move()
            money, cauldron = potages(money,cauldron)
        elif choice == "c":
            move()
            money,pet = owl_emporium(money,pet)
        elif choice == "d":
            move()
            money,supply_list = flourish_blotts(money,supply_list)
        elif choice == "e":
            move()
            money = fortescues(money)
        elif choice == "f":
            move()
            money = gringotts(money)
        elif choice == "g":
            move()
            money,wand,supply_list = ollivanders(money,wand,supply_list)
        elif choice == "h":
            show_list(supply_list)
        elif choice == "i":
            if wand == 0:
                print("You cannot go to Hogwarts without a wand!")
            else:
                print("Off the Hogwarts we go!")
                move()
                repeat = False

    time.sleep(1)


def quidditch_supplies(money,broom):

    return money,1

def owl_emporium(money,pet):
    
    return money,1

def flourish_blotts(money,supply_list):
    print("\nWelcome to Flourish and Blott's")
    repeat = True

    
    while repeat == True:
        choice = input("\n\nWhat would you like to do?"
              "\na) Buy all first year books"
              "\nb) Browse books"
              "\nc) Leave\n\n")

        if choice == "a":
            if money[0] < 13:
                print("You don't have enough Galleons (13) to pay for your wand.")
            else:
                print("You have acquired a full set of first year books")
                print("\n")
                money[0] -= 13
                print_money(money)
                for i in range(6):
                    supply_list[i][1] = 1

        elif choice == "b":
            print("You do a quick scan of the shelves and notice titles like")
            print("Most Macabre Monstrosities")
            time.sleep(1)
            print("Blood Borthers: My Life Amongst the Vampires")
            time.sleep(1)
            print("Curses and Counter-Curses")
            time.sleep(1)
            print("Death Omens: What to Do When You Know the Worst is Coming")

        elif choice == "c":
            repeat = False
            break

        choice = input("\nWould you like to do something else? ")

        if choice == "no" or choice == "No":
            repeat = False

    return money,supply_list

def fortescues(money):
    print("\nWelcome to Florean Fortescue's!")
    print("What can I get for you?")

    return money

def gringotts(money):

    print("\nWelcome to Gringotts.")
    repeat = True
    add_money = [0,0,0]
    while repeat == True:
        choice = input("\n\nWhat would you like to do?"
              "\na) Check your account balance"
              "\nb) Check how much money is in your pocket"
              "\nc) Withdraw money"
              "\nd) Leave\n\n")

        if choice == "a":
            print("You have infinite money in your account")
        elif choice == "b":
            print("You have "+str(money[0])+" Galleons, "+str(money[1])+" Sickles, and "+str(money[2])+" Knuts in your pocket")
        elif choice == "c":
            print("How much would you like to withdraw?")
            add_money[0] = int(input("Galleons: "))
            add_money[1] = int(input("Sickles: "))
            add_money[2] = int(input("Knuts: "))
            for i in range(3):
                money[i] += add_money[i]
            money = optimize_money(money)
        elif choice == "d":
            repeat = False
            break

        choice = input("Would you like to do something else? ")

        if choice == "no" or choice == "No":
            repeat = False

    print("\n\nBye now")
    
    return money

def ollivanders(money,wand,supply_list):

    print("\nWelcome to Ollivander's")
    repeat = True

    woods = ["ash","elm","hawthorn","holly","vine"]
    cores = ["dragon heartstring","unicorn hair","phoenix feather","basilisk horn","thestral hair"]
    
    while repeat == True:
        choice = input("\n\nWhat would you like to do?"
              "\na) Find a wand"
              "\nb) Learn about your wand"
              "\nc) Leave\n\n")

        if choice == "a":
            if money[0] < 7:
                print("You don't have enough Galleons (7) to pay for your wand.")
            else:
                print("The wand chooses the wizard...")
                print("I have just the one!")

                wand = [str(random.randint(16,24)/2)+" inches",
                        str(woods[random.randint(0,4)]),
                        str(cores[random.randint(0,4)])+" core"]
                print("\n"+wand[0]+", "+wand[1]+", "+wand[2])
                supply_list[6][1] = 1
                
                print("\nThat will be seven Galleons please")
                money[0] -= 7
                
                print("\nThank you!")
                print_money(money)
                
        elif choice == "b":
            if wand == ["","",""]:
                print("You don't have a wand")
            else:
                print(wand[0]+", "+wand[1]+", "+wand[2])
        elif choice == "c":
            repeat = False
            break

        choice = input("\nWould you like to do something else? ")

        if choice == "no" or choice == "No":
            repeat = False

    print("\nBye now")

    return money,wand,supply_list

def move():
    for i in range(5):
        time.sleep(0.3)
        print("\n...")

def optimize_money(money):
    if money[2] > 29:
        money[1] += int(money[2]/29)
        money[2] = money[2]%29
    if money[1] > 17:
        money[0] += int(money[1]/17)
        money[1] = money[1]%17
    money[3] = money[2]+29*money[1]+493*money[0]
    return money

def print_money(money):
    print("You have"
          "\n"+str(money[0])+" Galleons"
          "\n"+str(money[1])+" Sickles"
          "\n" +str(money[2])+" Knuts")

def show_list(supply_list):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("First-year students will require:")
    print("\nBooks:")
    for i in range(6):
        if supply_list[i][1] == 0:
            print("[ ] "+supply_list[i][0])
        else:
            print("[X] "+supply_list[i][0])
    print("\nOther Equipment:")
    for i in range(6,8):
        if supply_list[i][1] == 0:
            print("[ ] "+supply_list[i][0])
        else:
            print("[X] "+supply_list[i][0])
    print("\nStudents may also bring an Owl OR a Cat OR a Toad.")
    print("\nPARENTS ARE REMINDED THAT FIRST YEARS ARE NOT ALLOWED THEIR OWN BROOMSTICKS")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


main(money_global,wand_global,broom_global,pet_global,supply_list_global)

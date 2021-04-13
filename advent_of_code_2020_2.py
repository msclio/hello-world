

passwords = open('pass_list.txt').read().splitlines()

num_wrong = 0

for word in passwords:
    numbers = word.partition("-")
    first_num = numbers[0]
    sec_num = numbers[2].partition(" ")[0]
    passcode = numbers[2].partition(" ")[2]

print(num_wrong)

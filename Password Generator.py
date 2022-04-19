import random

letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z"]
special_characters = ["@", "#", "$", "%", "&"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

passwords_list = []

print("****Password generator****"
      "\nPlease choose your password, press 1 or 2:"
      "\n1. for short (8 characters)"
      "\n2. for long (12 characters)")
short_or_long = input()
next_password = True

if short_or_long == "1":
    while next_password == True:
        short_password = random.choices(letters_lower, k=2) + random.choices(letters_upper, k=2)\
                         + random.choices(special_characters, k=2) + random.choices(numbers, k=2)
        random.shuffle(short_password)
        passwords_list.append("".join(short_password))
        print(passwords_list)
        next_password = False
        if input("Press y for continue or anything to exit") == "y":
            next_password = True
        else:
            break

if short_or_long == "2":
    while next_password == True:
        long_password = random.choices(letters_lower, k=3) + random.choices(letters_upper, k=3)\
                         + random.choices(special_characters, k=3) + random.choices(numbers, k=3)
        random.shuffle(long_password)
        passwords_list.append("".join(long_password))
        print(passwords_list)
        next_password = False
        if input("Press y for continue or anything to exit") == "y":
            next_password = True
        else:
            break

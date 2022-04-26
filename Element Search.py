import random

random_list = sorted([random.randint(1, 99) for r in range(20)])
print(random_list)

number = int(input("Choose a number between 1 - 20."))

def find_number(list, num):
    start_index = 0
    end_index = len(list) - 1
    while True:
        mid_index = int((start_index + end_index) / 2)
        print(list[mid_index])
        if end_index < start_index:
            print("Your number is not on the list.")
            return False

        mid_number = list[mid_index]
        if num == mid_number:
            print("Your numer is in the list.")
            return True
        elif num < mid_number:
            end_index = mid_index - 1
        elif num > mid_number:
            start_index = mid_index + 1

print(find_number(random_list, number))
#with max() function
def max_number(one, two, three):
    print(f"A highest numeber is: {max([one, two, three])}")

max_number(1,2,3)

#without max() function
def max_number2():
    numbers = []
    sequence = ["first", "second", "third"]
    index = 0
    while len(numbers) <= 2:
        numbers.append(int(input(f"Pick {sequence[index]} number")))
        index += 1
    print(numbers)
    if numbers[0] > numbers[1] and numbers[0] > numbers[2]:
        print(f"{numbers[0]} is highest.")
    elif numbers[1] > numbers[0] and numbers[1] > numbers[2]:
        print(f"{numbers[1]} is highest.")
    else:
        print(f"{numbers[2]} is highest.")



max_number2()
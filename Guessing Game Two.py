def guess_game_two():
    num_list = [x for x in range(0, 101)]
    start_index = 0
    end_index = len(num_list)
    count = 1
    while True:
        if start_index == end_index:
            return False
        mid_index = int((start_index + end_index) /2)
        print(f"Is that your number {num_list[mid_index]}?\n1.Yes\n2.Lower\n3.Higher")
        answer = input()
        if answer == "1":
            print(f"I won! It took me only {count} try/tries!")
            return True
        elif answer == "2":
            end_index = mid_index
        elif answer == "3":
            start_index = mid_index
        count += 1

guess_game_two()

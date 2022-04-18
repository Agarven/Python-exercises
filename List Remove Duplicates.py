a = [1, 1, 2, 3, 3, 5, 8, 13, 21, 21, 34, 55, 89]
b = []

#1 with loop
def remove_duplicates():
    for number in a:
        if number not in b:
            b.append(number)
    print(b)

remove_duplicates()

#2 with sets
def remove_duplicates2():
    b = list(set(a))
    print(b)

remove_duplicates2()
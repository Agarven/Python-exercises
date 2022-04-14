def fibonacci():
    how_many = int(input("Ile chcesz wygenerwoać liczb z ciągu fibonacciego?"))
    count = 0
    fib1 = 0
    fib2 = 1
    if how_many == 0:
        print("Wybierz liczbę większą od 0.")
        fibonacci()
    elif how_many >= 1:
        print(fib2)
    while count <= (how_many-2):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        count += 1
        print(fib3)

fibonacci()
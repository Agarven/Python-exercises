number = int(input("Wpisz dowolną liczbę a podam Ci wszystkie jej dzielniki."))

divisors_range = range(1, number+1)
divisors = []

for i in divisors_range:
    print(i)
    if number % i == 0:
        divisors.append(i)
print(divisors)


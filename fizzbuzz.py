try:
    number = int(input("Please enter a number for fizzbuzz division (whole integers only, please): "))
except ValueError:
    number = int(input("Please enter an integer for fizzbuzz division: "))


while number > 0:
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number}: fizzbuzz")
    elif number % 5 == 0:
        print(f"{number}: buzz")
    elif number % 3 == 0:
        print(f"{number}: fizz")
    else:
        print(number)
    number = number - 1
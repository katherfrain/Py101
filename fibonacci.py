try:
    fibonacci = int(input("How many values of the Fibonacci sequence would you like to see? "))
except ValueError:
    fibonacci = int(input("Apologies, that was not an integer. Please enter another number: "))

fibonacci_incrementor = 0
fibonacci_printer = 0
add_for_fibonacci = []

print(fibonacci)
#while the incrementor is less than the number of values the user asked for, incremenet
while len(add_for_fibonacci) < fibonacci: 
    for x in range(fibonacci):
        add_for_fibonacci.append(fibonacci)
        fibonacci_printer = add_for_fibonacci + fibonacci
        print(fibonacci)

"""
    add_for_fibonacci.append(add_for_fibonacci[-1] + add_for_fibonacci[-2])
    print(add_for_fibonacci)

    # append the prior fibonacci number to the addition list
        add_for_fibonacci.append(fibonacci + fibonacci)
        print the sum of the fibonacci value + the added value (the prior list value)
    fibonacci_printer = fibonacci + add_for_fibonacci[fibonacci_incrementor]
"""
fibonacci_incrementor = fibonacci_incrementor + 1




try:
    fibonacci = int(input("How many values of the Fibonacci sequence would you like to see? "))
except ValueError:
    fibonacci = int(input("Apologies, that was not an integer. Please enter another number: "))

zerostart = 0 + fibonacci
onestart = fibonacci + fibonacci
add_for_fibonacci = [zerostart, onestart]

print(fibonacci)
while len(add_for_fibonacci) < fibonacci: 
    for x in range(fibonacci):
        add_for_fibonacci.append(add_for_fibonacci[-1] + add_for_fibonacci[-2])
        print(add_for_fibonacci)


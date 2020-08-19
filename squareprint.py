print("This program will print a square made of stars for dimensions X by Y.")
x = int(input("Please pick an integer input for X: "))
y = int(input("Please pick an integer input for Y: "))
count = 0

while count < x:
    print("*" * y)
    count = count + 1

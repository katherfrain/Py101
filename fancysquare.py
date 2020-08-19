print("This program will print a fancy square for dimensions X by Y.")
x = int(input("Please enter an integer value for X: "))
y = int(input("Please enter an integer value for Y: "))
count = 1
while count <= x:
    if count == 1 or count == x:
        print("*" * y)
    else:
        print("*",(" " * (y-4)), "*")
    count = count + 1
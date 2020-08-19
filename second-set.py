day = int(input("What day of the week is it, from 0-6 (0 being Monday)? "))
if day == 0:
    print("It is Monday.")
elif day == 1:
    print("It's Tuesday.")
elif day == 2:
    print("It is Wednesday, my dudes.")
elif day == 3:
    print("Thursday it is.")
elif day == 4:
    print("Friday, Friday, gotta get down on Friday.")
elif day == 5: 
    print("Saturday!")
elif day == 6: 
    print("Sunday!")
else:
    day = int(input(("I don't recognize that number, can you repeat a number between 0 and 6? ")))

if day == 5: 
    print("You can sleep in, it's the weekend!")
elif day == 6: 
    print("You can sleep in.")
else:
    print("Weekday - head to work!")

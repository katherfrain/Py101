bill_amount = float(input("What was the bill amount? Please don't include the dollar sign! "))
service_sort = input("What was the level of service, from poor to fair to excellent? ")
people_amount = int(input("And how many ways would you like to split that? "))
service_sort = service_sort.upper()

if service_sort == "POOR":
    tip_amount = (bill_amount*.1)
elif service_sort == "FAIR":
    tip_amount = (bill_amount*.15)
elif service_sort == "EXCELLENT":
    tip_amount = (bill_amount*.2)
else:
    bill_amount = float(input("I didn\'t understand your first statement. What amount did you owe, sans dollar sign? "))

total = bill_amount + tip_amount
perperson = float(total/people_amount)

print(f"Your tip is ${tip_amount:.2f}, and your total is ${total:.2f}, which splits to ${perperson:.2f} per person.")
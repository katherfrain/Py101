def want_another():
    do_you_want_another = input("Would you like to add to your list, yes/no? ")        
    if do_you_want_another == "yes":
        grocery = input("What would you like to add to your list? ")
        grocery_list.append(grocery)
        print("You have added ", grocery, "to the list")
        print("Your current list is: ", grocery_list)
        do_you_want_another = input("Would you like to add another item? Yes or no?")
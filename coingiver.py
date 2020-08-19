
keepgoing = True
coins = 0

while keepgoing == True:
    yeah = input(f"You have {coins} coins. Would you like another one? ")
    yeah = yeah.upper()
    if yeah == "YES" or yeah == "YEAH" or yeah == "YEA":
        coins = coins + 1
    else:
        keepgoing = False


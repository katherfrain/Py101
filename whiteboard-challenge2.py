def most_characters(stringy):
    letterlist = {}

    for letter in stringy:
        if letter in letterlist.keys():
            letterlist[letter] += 1
        else:
            letterlist[letter] = 1

    maxvalue = max(letterlist.values())
    print (maxvalue.letterlist)

    for values in letterlist.keys():
        if letterlist[values] == maxvalue:
            return values

print(most_characters('bbberteuisa'))
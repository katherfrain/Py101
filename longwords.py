string = input(" >")
printout = ''

for letters in range(len(string)):
    vowels = "aeiouAEIOU"
    if vowels in string[letters]:
        printout = printout + (string[letters] * 5)
    else:
        printout = printout + string[letters]

print(printout)
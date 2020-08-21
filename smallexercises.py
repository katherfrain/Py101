list = [1,3,4,5,6,888,9,43,130]

print(sum(list))
print(max(list))
print(min(list))

#exercise 4
for x in list:
    if x % 2 == 0:
        print(x)

#exercise 5
for y in list: 
    if y > 0:
        print(y)

#exercise 6
newlist = []
for i in list:
    if i > 0:
        newlist.append(i)

print(newlist)

#exercise 7
doubleprint = []
factor = 5

for j in list:
    doubleprint.append(j*factor)

print(doubleprint)

#exercise 8
string = input(" <")
backwards = string[::-1]
print(backwards)

list2 = [2333333, 1, 0]
biggestNumber = 0

for number in list2: 
    if number > biggestNumber:
        biggestNumber = number

print(biggestNumber)

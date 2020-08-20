triangle_height = int(input("How many lines would you like this triangle to be? "))
triangle_iterator = int(triangle_height+1)
count = 0

while count < triangle_height:
    count = count + 1
    triangle_iterator = triangle_iterator - 1
    if count == 1:
        print((" " * triangle_iterator), ("*" * count))
    else:
        print((" " * triangle_iterator), ("*" * ((count*2)-1)))


    
    
"""_________
|__|__|__|
|__|__|__|
|__|__|__|
|__|__|__|
"""

board_height = int(input("How many rows would you like your Tic-Tac-Toe board to have? "))
board_width = int(input("And how many columns would you like it to have? "))
counter = 0
boxvalue = "|__"
length_of_box = 0
height_of_box = 0 

#the first line will be constructed differently
# because the top row is just a row of underscores
print("_" * (board_width-1))

#makes the rest of the board
while length_of_box < board_width:
    if height_of_box < board_height:
        print(boxvalue*board_width)
        height_of_box = height_of_box + 1 
    elif height_of_box == board_width:
        print("|")

wincondition = False
print("Welcome to Tic-Tac-Toe")
print("The Tic-Tac-Toe board can be considered to follow a standard grid pattern.")
print("So the top-left corner is 1A, the box after that is 2A, etc.")

while wincondition == False:
    userX = int(input("Pick a box to put your X into!"))

    
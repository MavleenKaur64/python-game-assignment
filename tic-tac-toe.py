import random

# create an empty list for markers (index 1–9 used)
li = [" "] * 10

def display(li):
    print(li[7], "|", li[8], "|", li[9])
    print("-" * 9)
    print(li[4], "|", li[5], "|", li[6])
    print("-" * 9)
    print(li[1], "|", li[2], "|", li[3])

def check_win():
    return (li[7]==li[8]==li[9]!=" ") or \
           (li[4]==li[5]==li[6]!=" ") or \
           (li[1]==li[2]==li[3]!=" ") or \
           (li[7]==li[4]==li[1]!=" ") or \
           (li[8]==li[5]==li[2]!=" ") or \
           (li[9]==li[6]==li[3]!=" ") or \
           (li[1]==li[5]==li[9]!=" ") or \
           (li[7]==li[5]==li[3]!=" ")


def takeposition():
    # creating a placeholder for the position

    position = None

    # a loop till current input is in place
    while not position:

        # taking input - position
        position = input("Enter position (1-9):")

        # checking if the input is int
        if not position.isnumeric():
            # resetting the position if input not int
            position = None
        # checking input if it is in range (1 to 10)   
        elif not int(position) in range(1,10):
            # restting the position if input is not in range
            position = None
        # checking for blank space in the list    
        elif not li[int(position)] == " ":
            position = None
        print("\n"*3)    
    # returning the int type position as input is always in string        
    return int(position)

def ChangeMarker(marker):
    """exchanging marker O - X"""
    if marker == "X":
        return "O"
    return "X"  

def players_name():
    player_1 = input("Enter your name-Player 1")
    player_2 = input("Enter your name-Player 2")
    return player_1,player_2


# main game

player_1,player_2 = players_name()
player = "X"
print("Welcome to Tic Tac Toe!")
for i in range(9):
    display(li)
    move = takeposition()
    li[move] = player

    if check_win():
        display(li)
        winner_name = player_1 if player == "X" else player_2
        print(f"Player {winner_name} ({player}) wins!")
        break
    player = ChangeMarker(player)
    
else:
    display(li)
    print("It's a draw!")

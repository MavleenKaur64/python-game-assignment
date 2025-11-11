
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

player = "X"
for turn in range(9):
    display(li)
    move = int(input(f"Player {player}, choose (1-9): "))

    if li[move] != " ":
        print("That spot is taken! Try again.")
        continue

    li[move] = player

    if check_win():
        display(li)
        print(f"Player {player} wins!")
        break

    # switch player
    player = "O" if player == "X" else "X"
else:
    display(li)
    print("It's a draw!")

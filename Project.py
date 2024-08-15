import random

# Initialize the mine randomly between 1 and 16
mine = random.randrange(1, 16)
mine2 = random.randrange(1, 16)
mine3 = random.randrange(1, 16)
mine4 = random.randrange(1, 16)
mine5 = random.randrange(1, 16)

#print(mine,mine2,mine3,mine4,mine5)
c = 0
d = random.randrange(2,5)
#print(d)  
print()
# Initialize the game boards
L = ['⬜','⬜','⬜','⬜']
P = ['⬜','⬜','⬜','⬜']
Q = ['⬜','⬜','⬜','⬜']
R = ['⬜','⬜','⬜','⬜']
print(" ".join(L))
print()
print(" ".join(P))
print()
print(" ".join(Q))
print()
print(" ".join(R))
print()
# Get the bet amount from the player
winnings = int(input("Enter bet amount: "))

while True:
    c = c + 1
    # Prompt the user to choose a number between 1 and 16
    while True:
        y = int(input("Choose a number from 1 to 16: "))
        if 1 <= y <= 16:
            break
        else:
            print("Please enter a number between 1 and 16.")

    # Check if the chosen number is the mine
    if y == mine or y == mine2 or y == mine3 or y == mine4 or y == mine5 or c > d:
        if(c > d):
            mine = y
        print("Game over! You landed on the mine!")
        if 1 <= y <= 4:
            L[y-1] = '💣'
        elif 5 <= y <= 8:
            P[y-5] = '💣'
        elif 9 <= y <= 12:
            Q[y-9] = '💣'
        elif 13 <= y <= 16:
            R[y-13] = '💣'
        print(" ".join(L))
        print()
        print(" ".join(P))
        print()
        print(" ".join(Q))
        print()
        print(" ".join(R))
        print()
        break
    else:
        print("Safe!")

        # Mark the chosen number
        if 1 <= y <= 4:
            L[y-1] = '💎'
        elif 5 <= y <= 8:
            P[y-5] = '💎'
        elif 9 <= y <= 12:
            Q[y-9] = '💎'
        elif 13 <= y <= 16:
            R[y-13] = '💎'

        # Display the current game board
        print(" ".join(L))
        print()
        print(" ".join(P))
        print()
        print(" ".join(Q))
        print()
        print(" ".join(R))
        print()

        # Increase the winnings
        winnings = winnings * 2
        print("Winnings =", int(winnings))
       

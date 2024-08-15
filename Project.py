import random
mines = int(input('Enter Number of Mines you Want '))

if mines == 1:
  print('There is only 1 Mine!')
  x = random.randrange(1,9)
  L = ['■','■','■']
  P = ['■','■','■']
  Q = ['■','■','■']
  bet = int(input("Enter bet amount: "))
  winnings = bet

  while True:
      cnt = len(L)

      while True:
          y = int(input("Choose a number from 1 to 9: "))
          if 1 <= y <= 9:
              break
          else:
              print("Please enter a number between 1 and 9.")

      if y == x:
          print("Game over! You landed on the mine!")
          print(L)
          print(P)
          print(Q)
          break
      elif y in L:
          print("You already chose this number. Choose another one.")
      else:
        print("Safe! ")
        if 1 <= y <= 3:
              L[y-1] = '◈'
              
        elif 4 <= y <= 6:
            if y == 4:
                P[0] = '◈'
            elif y == 5:
                P[1] = '◈'
            elif y == 6:
                P[2] = '◈'
        elif 7 <= y <= 9:
            if y == 7:
                Q[0] = '◈'
            elif y == 8:
                Q[1] = '◈'
            elif y == 9:
                Q[2] = '◈'
        print("Numbers Chosen:")
        print(char(L))
        print(P)
        print(Q)
        winnings = winnings * 1.2
        print("Winnings =", int(winnings))
        cont = input("Continue? (y/n): ")
        if cont.lower() != "y":
            print("Game terminated")
            print("You Won", winnings, "Rupees")
            break

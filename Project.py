import random
import mysql.connector

print("Welcome to the Ultimate Minesweeper Game!")
print("Your adventure begins now!\n")

conn = mysql.connector.connect(host="localhost", user="root", password="SQL1234", database="Minesweeper")
cursor = conn.cursor()

def check_user_balance(name):
    cursor.execute("SELECT Balance FROM Data WHERE Name = '" + name + "'") 
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def update_user_balance(name, balance):
    cursor.execute("UPDATE Data SET Balance = " + str(balance) + " WHERE Name = '" + name + "'")
    conn.commit()

def create_user(name):
    cursor.execute("INSERT INTO Data (Name, Balance) VALUES ('" + name + "', 0)")
    conn.commit()

def deposit(balance):
    amount = int(input("Enter the amount to deposit: "))
    balance += amount
    print(f"₹{amount} deposited. New balance: ₹{balance}")
    return balance

def withdraw(balance):
    amount = int(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn. New balance: ₹{balance}")
    return balance

def play_game(balance):
    if balance <= 0:
        print("You need to deposit money to play the game.")
        return balance

    print("Playing the game...")

    mine_position = random.randrange(1, 17)  # Mine Position

    bet = int(input("Enter bet amount: "))

    if bet > balance:
        print("You don't have enough balance for this bet. Try again.")
        return balance
    else:
        balance -= bet

    L = ['⬜', '⬜', '⬜', '⬜']
    P = ['⬜', '⬜', '⬜', '⬜']
    Q = ['⬜', '⬜', '⬜', '⬜']
    R = ['⬜', '⬜', '⬜', '⬜']

    def display_board():
        print(" ".join(L))
        print()
        print(" ".join(P))
        print()
        print(" ".join(Q))
        print()
        print(" ".join(R))
        print()

    print("Welcome to the Minesweeper Game!")
    display_board()

    while True:
        while True:
            try:
                y = int(input("Choose a number from 1 to 16: "))
                if 1 <= y <= 16:
                    break
                else:
                    print("Please enter a number between 1 and 16.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if y == mine_position:
            print("Game over! You landed on a mine!")
            if 1 <= y <= 4:
                L[y - 1] = '💣'
            elif 5 <= y <= 8:
                P[y - 5] = '💣'
            elif 9 <= y <= 12:
                Q[y - 9] = '💣'
            elif 13 <= y <= 16:
                R[y - 13] = '💣'
            display_board()

            print(f"You lost {bet}! Remaining balance: {balance}")
            update_user_balance(name, balance)
            break
        else:
            print("Safe!")

            if 1 <= y <= 4:
                L[y - 1] = '💎'
            elif 5 <= y <= 8:
                P[y - 5] = '💎'
            elif 9 <= y <= 12:
                Q[y - 9] = '💎'
            elif 13 <= y <= 16:
                R[y - 13] = '💎'

            display_board()

            bet *=2   # Increase bet only if the player survives
            print(f"Winnings = {int(bet)}")

            while True:
                choice = input("Do you want to continue playing or exit? (continue/exit): ").lower()
                if choice == "continue":
                    break
                elif choice == "exit":
                    balance += bet
                    print(f"You have exited the game with {int(bet)} added to your balance. Your new balance is {balance}")
                    update_user_balance(name, balance)
                    return balance
                else:
                    print("Invalid choice. Please type 'continue' or 'exit'.")

name = input("Enter your name: ")
balance = check_user_balance(name)
if balance is None:
    create_user(name)
    balance = 0

while True:
    print("Choose an option:")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Play the game")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        balance = deposit(balance)
        update_user_balance(name, balance)
    elif choice == '2':
        balance = withdraw(balance)
        update_user_balance(name, balance)
    elif choice == '3':
        balance = play_game(balance)
    elif choice == '4':
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

conn.close()

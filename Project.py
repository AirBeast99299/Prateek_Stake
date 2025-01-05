import random
import mysql.connector

print("Welcome to the Ultimate Minesweeper Game!")
print("Your adventure begins now!\n")

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="SQL1234", database="Minesweeper")
    cursor = conn.cursor()

    def check_user_balance(name):
        sql = f"SELECT Balance FROM Data WHERE Name = '{name}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def update_user_balance(name, balance):
        sql = f"UPDATE Data SET Balance = {balance} WHERE Name = '{name}'"
        cursor.execute(sql)
        conn.commit()

    def create_user(name):
        sql = f"INSERT INTO Data (Name, Balance) VALUES ('{name}', 0)"
        cursor.execute(sql)
        conn.commit()

    def deposit(balance):
        while True:
            try:
                amount = int(input("Enter the amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print("₹", amount, " deposited. New balance: ₹", balance)
                    return balance
                else:
                    print("Please enter a valid amount.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def withdraw(balance):
        while True:
            try:
                amount = int(input("Enter the amount to withdraw: "))
                if amount > 0 and amount <= balance:
                    balance -= amount
                    print("₹", amount, " withdrawn. New balance: ₹", balance)
                    return balance
                elif amount > balance:
                    print("Insufficient balance.")
                else:
                    print("Please enter a valid amount.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play_game(balance):
        if balance <= 0:
            print("You need to deposit money to play the game.")
            return balance

        print("Playing the game...")

        mine_position = random.randrange(1, 17)  # Mine Position

        while True:
            try:
                bet = int(input("Enter bet amount: "))
                if bet > 0 and bet <= balance:
                    break
                elif bet > balance:
                    print("You don't have enough balance for this bet. Try again.")
                else:
                    print("Please enter a valid bet amount.")
            except ValueError:
                print("Invalid input. Please enter a number.")

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

                print("You lost ₹", bet, "! Remaining balance: ₹", balance)
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

                bet *= 2  # Increase bet only if the player survives
                print("Winnings = ₹", int(bet))

                while True:
                    choice = input("Do you want to continue playing or exit? (continue/exit): ").lower()
                    if choice == "continue":
                        break
                    elif choice == "exit":
                        balance += bet
                        print("You have exited the game with ₹", int(bet), " added to your balance. Your new balance is ₹", balance)
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

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if conn.is_connected():
        conn.close()

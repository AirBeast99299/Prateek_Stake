import random
import mysql.connector

# Connect to MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",  # Replace with your MySQL username
        password="your_password",  # Replace with your MySQL password
        database="minesweeper_game"
    )

# Fetch or create a player record
def get_or_create_player(name):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM players WHERE name = %s", (name,))
    result = cursor.fetchone()

    if result:
        balance = result[0]
    else:
        balance = 0
        cursor.execute("INSERT INTO players (name, balance) VALUES (%s, %s)", (name, balance))
        conn.commit()

    conn.close()
    return balance

# Update player balance
def update_balance(name, balance):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE players SET balance = %s WHERE name = %s", (balance, name))
    conn.commit()
    conn.close()

# Deposit function
def deposit(balance):
    amount = int(input("Enter the amount to deposit: "))
    balance += amount
    print("You have successfully deposited", amount, "Your new balance is", balance)
    return balance

# Withdraw function
def withdraw(balance):
    while True:
        amount = int(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance. Please enter a smaller amount.")
        else:
            balance -= amount
            print("You have successfully withdrawn", amount, "Your new balance is", balance)
            return balance

# Play game function
def play_game(balance):
    if balance <= 0:
        print("Insufficient balance to play. Please deposit money first.")
        return balance

    mine_positions = random.sample(range(1, 17), 5)  # Place 5 mines randomly
    c = 0
    d = random.randint(2, 5)
    winnings = int(input("Enter bet amount: "))

    if winnings > balance:
        print("You don't have enough balance for this bet. Try again.")
        return balance

    balance -= winnings

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
        c += 1

        while True:
            y = int(input("Choose a number from 1 to 16: "))
            if 1 <= y <= 16:
                break
            else:
                print("Please enter a number between 1 and 16.")

        if y in mine_positions or c > d:
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
            print("You lost", winnings, "! Remaining balance:", balance)
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

            winnings *= 2
            print("Winnings =", int(winnings))

            while True:
                choice = input("Do you want to continue playing or exit? (continue/exit): ").strip().lower()
                if choice == "continue":
                    break
                elif choice == "exit":
                    balance += winnings
                    print("You have exited the game with", int(winnings), "added to your balance. Your new balance is", balance)
                    return balance
                else:
                    print("Invalid choice. Please type 'continue' or 'exit'.")

    return balance

# Main function
def main():
    print("Welcome to the Ultimate Minesweeper Game!")
    name = input("Enter your name: ")
    balance = get_or_create_player(name)

    while True:
        print("Choose an option:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Play the game")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            balance = deposit(balance)
            update_balance(name, balance)
        elif choice == '2':
            balance = withdraw(balance)
            update_balance(name, balance)
        elif choice == '3':
            balance = play_game(balance)
            update_balance(name, balance)
        elif choice == '4':
            print("Thank you for playing! Goodbye!")
            update_balance(name, balance)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

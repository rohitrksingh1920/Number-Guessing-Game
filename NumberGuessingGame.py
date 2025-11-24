import numpy as np
import pandas as pd

history = []  # store game results


def play_game():
    print(" Number Guessing Game")

    print("""
Choose difficulty:
1. Easy    (1–50,    10 attempts)
2. Medium  (1–100,   7 attempts)
3. Hard    (1–200,   5 attempts)
""")

    # Select difficulty
    choice = int(input("Select level (1/2/3): "))

    if choice == 1:
        level = "Easy"
        max_num, attempts = 50, 10
    elif choice == 2:
        level = "Medium"
        max_num, attempts = 100, 7
    else:
        level = "Hard"
        max_num, attempts = 200, 5

    # Generate number using NumPy
    number = np.random.randint(1, max_num + 1)
    initial_attempts = attempts

    print(f"\nI'm thinking of a number between 1 and {max_num}. Good luck!\n")

    # Game loop
    while attempts > 0:
        guess = int(input(f"Attempts left {attempts} → Your guess: "))
        attempts -= 1

        if guess < number:
            print("Too low!\n")
        elif guess > number:
            print("Too high!\n")
        else:
            print("Correct guess! You win!")

            # Add result to history
            history.append([level, initial_attempts - attempts, "Win", number])
            return

    print(f"You lost! The number was {number}.")
    history.append([level, initial_attempts, "Lose", number])


# Game loop
while True:
    play_game()
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        break

# Save history using pandas
df = pd.DataFrame(history, columns=["Level", "Attempts_Used", "Result", "Number"])
df.to_csv("game_history.csv", index=False)

print("\nGame history saved as 'game_history.csv'")
print(df)

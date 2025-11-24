import numpy as np

def play_game():
    print("\n🎮 Number Guessing Game")

    print("""
Choose difficulty:
1. Easy    (1–50,    10 attempts)
2. Medium  (1–100,   7 attempts)
3. Hard    (1–200,   5 attempts)
""")

    choice = int(input("Select level (1/2/3): "))

    if choice == 1:
        max_num, attempts = 50, 10
    elif choice == 2:
        max_num, attempts = 100, 7
    else:
        max_num, attempts = 200, 5

    # Using numpy for random number
    number = np.random.randint(1, max_num + 1)

    print(f"\nI'm thinking of a number between 1 and {max_num}. Good luck!\n")

    while attempts > 0:
        guess = int(input(f"Attempts left {attempts} → Your guess: "))
        attempts -= 1

        if guess < number:
            print("⬆️ Too low!\n")
        elif guess > number:
            print("⬇️ Too high!\n")
        else:
            print("🎉 Correct guess! You win!")
            return

    print(f"❌ You lost! The number was {number}.")

# Game loop
while True:
    play_game()
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print("👋 Thanks for playing!")
        break

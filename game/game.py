import random

def guessing_game():
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Guessing Game! I have selected a number between 1 and 100.")

    # Game loop
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You guessed the correct number in", attempts, "attempts!")
            return  # End the game
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    # If the player runs out of attempts
    print("Sorry, you've run out of attempts. The correct number was", secret_number)

# Start the game
guessing_game()
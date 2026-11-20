import random  # Use Python's random number generator.

number = random.randint(1, 100)  # Pick a number from 1 to 100.
print("Guess a number between 1 and 100.")

while True:  # Keep playing until the number is guessed.
    guess = input("Your guess: ").strip()  # Read the user's guess.

    if not guess.isdigit():  # Reject input that is not a number.
        print("Please enter a whole number.")
        continue

    guess = int(guess)  # Convert the guess to a number.
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
        break  # End the game.

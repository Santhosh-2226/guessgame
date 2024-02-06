import random
def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = int(input("Enter the maximum number of attempts: "))
    print("Welcome to the Guess the Number game!")
    print("I've picked a number between 1 and 100. Try to guess it!")
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
                return
        except ValueError:
            print("Please enter a valid integer.")
    
    print(f"Sorry, you've used up all {max_attempts} attempts. The number was {secret_number}.")

guess_the_number()

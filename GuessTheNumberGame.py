import random

print("----- THE GUESSING GAME -----")
print("The machine will pick a number randomly.")
print("Type a number and I'll tell you if it's higher or lower.")
print("Find the number and win! You have 6 tries.\n")

secret = random.randint(1, 100)
attempts = 0
max_attempts = 6

while attempts < max_attempts:
    playerGuess = int(input("Enter a number: "))
    attempts += 1

    if playerGuess == secret:
        print("🎉 You got it! The number was:", secret)
        print("You guessed it in", attempts, "tries.")
        break
    elif playerGuess > secret:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

# if loop ends without break
if attempts == max_attempts and playerGuess != secret:
    print("\n😢 Game over! The number was:", secret)

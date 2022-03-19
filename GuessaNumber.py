import random
import math

min = int(input("Min bound: "))
max = int(input("Max bound: "))

x = random.randint(min, max)
print("The number of guesses you can make", int(math.sqrt(max)))

counter = 0

while counter < int(math.sqrt(max)):
    counter += 1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("\nCongratulations! You got the number in", counter, "tries")
        break

    elif x > guess:
        print("\nGuess a bigger number")

    elif x < guess:
        print("\nGuess a smaller number")

    if guess >= int(math.sqrt(max)):
        print("The number is", x)
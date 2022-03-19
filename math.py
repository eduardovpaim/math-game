import random
import math

lower = int(input("Emter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congratulations you did it in ", count, " try")

        break
    elif x > guess:
        print("you guessed to small")
    elif x < guess:
        print("you guessed to high")

if count >= math.log(upper - lower + 1, 2):
    print("\nthe number is %d"%x)
    print("\tbetter luck next time")

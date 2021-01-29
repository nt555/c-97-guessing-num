import random

print("Number guessing game")
num = random.randint(1, 9)
i = 0

print("Guess a number (between 1 and 9):")

while i < 5:
    value = int(input("Enter your guess:- "))
    if value == num:
        print("Congratulation YOU WON!!!")
        break
    elif value < num:
        print("Your guess was too low: Guess a number higher than", value)
    else:
        print("Your guess was too high: Guess a number lower than", value)
    i += 1
if not i < 5:
    print("YOU LOSE!!! The number is", num)

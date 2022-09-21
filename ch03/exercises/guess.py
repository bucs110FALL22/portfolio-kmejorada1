import random

num = random.randrange(1,10)
guess = int(input("Guess a number between 1 and 10 "))

i = 0
for i in range(0,3):
  if guess == num:
    print("You guessed correctly!")
    break
  elif guess < num:
    print("Your guess was too low!")
    guess = int(input("Guess a number between 1 and 10 "))
  elif guess > num:
    print("Your guess was too high!")
    guess = int(input("Guess a number between 1 and 10 "))
  else:
    print("You're out of guesses!")
    break
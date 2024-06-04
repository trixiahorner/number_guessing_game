#number guessing game

import random
import art 

#Display game log
print(art.logo)

#Generate random number 1-100
rand_num = random.randint(1, 100)
print("\nI'm thinking of a number between 1 and 100.")

#Uncomment next line to reveal random number. For debugging.
#print(f"pssst, the random number to guess is {rand_num}")

#Dictionary to store number of tries for each difficulty level
difficulty_levels = {
    "easy": 10,
    "hard": 5
}

#Prompt user to select difficulty level
while True:
  difficulty = input("\nChoose a difficulty level. Type 'easy' or 'hard': ").lower()
  if difficulty in difficulty_levels:
    num_tries = difficulty_levels[difficulty]
    break
  else:
    print("\n***Invalid option. Try again.***")

#Main game loop
while num_tries != 0:
  print(f"\nYou have {num_tries} attempts remaining")
  user_guess = int(input("Make a guess: "))

  if user_guess == rand_num:
    print(f"You got it! The answer was {rand_num}.")
    break
  elif user_guess > rand_num:
    print("Too high. Guess again.")
  else:
    print("Too low. Guess again.")
    
  num_tries -= 1

#End of game message if user runs out of tries
if num_tries == 0:
  print("\nOut of guesses. You lose.")
  print(f"The correct number was {rand_num}")


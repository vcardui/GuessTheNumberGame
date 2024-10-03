import random
from art import logo

print(logo)

random_number = random.randint(0,100)
user_attempts = 0

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {random_number}")

ok_input = False
while ok_input == False:
  difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))

  if difficulty == 'easy':
    ok_input = True
    user_attempts = 10
    #print("easy")

  elif difficulty == 'hard':
    ok_input = True
    user_attempts = 5
    #print("hard")

  else:
    print("   Please type a valid answer...")

while 0 < user_attempts:
  #global random_number
  #global user_attempts

  right_type = False
  while right_type == False:
    user_guess = input("Make a guess: ")
    
    if user_guess.replace("-","").isdigit():
      user_guess = int(user_guess)
      right_type = True
    else:
      print("   Please type a valid answer...")

  if user_guess == random_number:
    print(f"You got it! The answer was {random_number}.")

  elif random_number < user_guess:
    user_attempts -= 1
    print("Too high.")
    print(f"Guess again. \nYou have {user_attempts} attempts remaining to guess the number.")

  elif user_guess < random_number:
    user_attempts -= 1 
    print("Too low.")
    print(f"Guess again. \nYou have {user_attempts} attempts remaining to guess the number.")

if user_attempts == 0:
    print("You've run out of guesses, you lose.")
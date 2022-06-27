from random import randint
from art import logo


def chose_num():
   return randint(1,100)

def compare_num(selected_num, guessed_num): 
  if selected_num > guess_num:
    print("Too low.")
    print("Try again!")
  elif selected_num < guessed_num:
    print("Two High.")
    print("Try again!")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100")
is_game_over = False
chosen_num = int(chose_num())
print(chosen_num)

difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  num = 10
elif difficulty == "hard":
  num = 5

for _ in range(num):
  count = num
  while not is_game_over:
    print(f"You have {count} attempts remaining to guess the number: ")
    guess_num = int(input("Make a guess: "))
    
    count -= 1

    if chosen_num == guess_num:
      print(f"You got it! The answer was {chosen_num}.")
      is_game_over = True
    elif count == 0:
      print(f"Pssst, the correct answer was {chosen_num}.")
      print("You ran out of guesses, You lose!")
      is_game_over = True
    else:
      compare_num(chosen_num, guess_num)
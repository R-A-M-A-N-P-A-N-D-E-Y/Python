# import the dictionary
# chose two random peson
# compare both based on followers
# if guessed correct then chose a new person and compare it with 2nd chosen person
# keep adding scores
# keep it runing until user guesses wrong
# import and use art

from art import logo, vs
import random
from game_data import data 
from replit import clear

def select_person(data):
  return random.choice(data)

first_person = select_person(data)
second_person = select_person(data)

while first_person == second_person:
  second_person = select_person(data)

end_game = False
score = 0

print(logo)

while not end_game:
  print(f"Compare A: {(first_person['name'])}, a {(first_person['description'])} form {(first_person['country'])}")

  print(vs)
  
  print(f"Compare B: {(second_person['name'])}, a {(second_person['description'])} form {(second_person['country'])}")
  
  guess = input("Who has more followers? Type 'A' or 'B': ")
  
  if guess == "A" or guess == "a":
    
    if first_person["follower_count"] > second_person["follower_count"]:
      score += 1
      clear()
      print(logo)
      print(f"You are right! Current Score: {score}")
      first_person = second_person
    elif first_person["follower_count"] < second_person["follower_count"]:
      clear()
      print(logo)
      print(f"Sorry that's wrong. Final sore : {score}")
      end_game = True
      
  elif guess == "B" or guess == "b":
    
    if first_person["follower_count"] > second_person["follower_count"]:
      score += 1
      clear()
      print(logo)
      print(f"You are right! Current Score: {score}")
      first_person = second_person
    elif first_person["follower_count"] < second_person["follower_count"]:
      clear()
      print(logo)
      print(f"Sorry that's wrong. Final sore : {score}")
      end_game = True
      
  second_person = select_person(data)
  
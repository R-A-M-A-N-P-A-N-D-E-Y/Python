import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.  "))
computer_move = [rock, paper, scissors]
length = len(computer_move)
computer_choice = random.randint(0,2)
if user_move >= 3 or user_move < 0: 
  print("You typed an invalid number, you lose!")
else:
  user_choice = computer_move[user_move]
  Computer_choice = computer_move[computer_choice]
  if computer_choice == user_move:
    print(user_choice)
    print("\nComputer choose:\n")
    print(Computer_choice)
    print("\nIs'a a draw!")
  elif computer_choice == 0 and user_move == 1:
    print(user_choice)
    print("\nComputer choose:\n")
    print(Computer_choice)
    print("\nYou Won!")
  elif computer_choice == 0 and user_move == 2:
    print(user_choice)
    print("\nComputer choose:\n")
    print(Computer_choice)
    print("\nYou Lost!")
  elif computer_choice == 1 and user_move == 0:
    print(user_choice)
    print("\nComputer choose:\n")
    print(Computer_choice)
    print("\nYou Lost!")
  elif computer_choice == 1 and user_move == 2:
    print(user_choice)
    print("\nComputer choose:\n")
    print(Computer_choice)
    print("\nYou Won!")
  elif computer_choice == 2 and user_move == 0:
    print(user_choice)
    print("\nComputer choose:\n")
    print(Computer_choice)
    print("\nYou Won!")
  elif computer_choice == 2 and user_move == 1:
    print(user_choice)
    print("\nComputer choose:\n")
    print(Computer_choice)
    print("\nYou Lost!")
    




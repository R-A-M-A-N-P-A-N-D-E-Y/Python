print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
first_decision = input('You are at a road cross. Where do you want to go? Type "left" or "right"\n')print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
first_decision = input('You are at a road cross. Where do you want to go? Type "left" or "right"\n').lower()
if first_decision == "left":
  print("You Fell in a Hole. Game Over..!\n")
else:
  second_decision = input('You came to a lake. There is an island in the middle of the lake. Type "swim" to swim across or Type "wait" to wait for a boat.\n').lower()
  if second_decision == "swim":
    print("You got eaten by a crocodyle. Game Over..!\n")
  else:
    third_decision = input('You arrived at the island unharmed. There is a house with 3 doors. One red, One yellow and One blue. Which colour do you choose?\n').lower()
    if third_decision == "red":
      print("You got burned in flames. Game Over..!\n")
    elif third_decision == "blue":
      print("You got frozen in ice. Game Over..!\n")
    else:
      print("Congratulations, You Found The Treasure. You Won..!\n")

if first_decision == "left":
  print("You Fell in a Hole. Game Over..!\n")
else:
  second_decision = input('You came to a lake. There is an island in the middle of the lake. Type "swim" to swim across or Type "wait" to wait for a boat.\n')
  if second_decision == "swim":
    print("You got eaten by a crocodyle. Game Over..!\n")
  else:
    third_decision = input('You arrived at the island unharmed. There is a house with 3 doors. One red, One yellow and One blue. Which colour do you choose?\n')
    if third_decision == "red":
      print("You got burned in flames. Game Over..!\n")
    elif third_decision == "blue":
      print("You got frozen in ice. Game Over..!\n")
    else:
      print("Congratulations, You Found The Treasure. You Won..!\n")

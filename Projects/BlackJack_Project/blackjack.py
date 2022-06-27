import random
from replit import clear
from art import logo

def deal_cards():
  """"It gives randam card to user and computer."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(card):
  """It calculates the total score."""
  if sum(card) == 21 and len(card) == 2:
    return 0
  if 11 in card and sum(card) > 21:
    card.remove(11)
    card.append(1)
  return sum(card)

def compare_score(user_score, dealer_score):
  """Compares user's score with computer's score and tells the winner."""
  if user_score == dealer_score:
    return "Draw 🙃"
  elif dealer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif dealer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > dealer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  dealer_card = []  
  user_card = []
  for cards in range(2):
    user_card.append(deal_cards())
    dealer_card.append(deal_cards())
      
  is_game_over = False
  while not is_game_over: 
    user_total = calculate_score(user_card)
    dealer_total = calculate_score(dealer_card)
    
    print(f"Your cards are {user_card}, total count is {user_total}")
    print(f"Dealer's First card is {dealer_card[0]}")
    
    
    if user_total == 0 or dealer_total == 0 or user_total > 21:
      is_game_over = True
    else:
      should_contineu = input("Type 'y' to get another card, type 'n' to pass: ")
      if should_contineu == "y":
        user_card.append(deal_cards())
        user_total = calculate_score(user_card)
      else:
        is_game_over = True
  
  while dealer_total != 0 and dealer_total < 17:
    dealer_card.append(deal_cards())
    dealer_total = calculate_score(dealer_card)
  
  print(f"   Your final hand: {user_card}, final score: {user_total}")
  print(f"   Your final hand: {dealer_card}, final score: {dealer_total}")
  print(compare_score(user_total, dealer_total))

while not input("Do you want ot play a game of blackjack, type 'y' or 'n': ") != "y":
  clear()
  print(logo)
  play_game()


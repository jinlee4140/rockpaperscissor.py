import random

choose = ["rock", "paper", "scissor"]


player_choice = raw_input(">")
ai_choice = random.choice(choose)

print ai_choice
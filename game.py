import random

choose = ["rock", "paper", "scissor"]


player_choice = raw_input(">")
ai_choice = random.choice(choose)

player_score = 0
ai_score = 0



# while player_score == 2 or ai_score == 2:
print "Player Score: %d, Computer Score: %d" % (player_score, ai_score)






print ai_choice
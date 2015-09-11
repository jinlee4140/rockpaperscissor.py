import random


def rockpaperscissors():
	choose = ["rock", "paper", "scissor"]

	player_score = 0
	ai_score = 0



	while player_score == 2 or ai_score == 2:
		print "Player Score: %d, Computer Score: %d" % (player_score, ai_score)
		print "Choose rock, paper, or scissor"

		player_choice = raw_input(">")
		ai_choice = random.choice(choose)

		if player_choice == ai_choice:
			print "It is tied, try again!!!!"
		elif player_choice == "rock" and ai_choice == "scissor":
			print "Player won!"
			player_score = player_score + 1
		elif player_choice == "scissor" and ai_choice == "paper":
			print "Player won!"
			player_score = player_score + 1
		elif player_choice == "paper" and ai_choice == "rock":
			print "Player won!"
			player_score = player_score + 1
		elif player_choice == "rock" and ai_choice == "paper":
			print "Comp won"
			ai_score = ai_score + 1
		elif player_choice == "paper" and ai_choice == "scissor":
			print "Comp won"
			ai_score = ai_score + 1
		elif player_choice == "scissor" and ai_choice == "rock":
			print "Comp won"
			ai_score = ai_score + 1



		if ai_score > player_score:
			print "Computer wins"
		else
			print "Player wins"

			
rockpaperscissors()





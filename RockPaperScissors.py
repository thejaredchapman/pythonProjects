import random

def play():
	# setting up game 
	user = input("'r for rock, 'p' for paper, 's' for scissors")
	computer = random.choice(['r','p','s'])

	# setting up responses
	if user == computer:
		return 'It\'s a tie'

	if is_win(user, computer):
		return 'You won!'

	return 'You lost!'

def is_win(player,opponent):
	# setting up parameters to return true

	if (player = 'r' and opponent ='s') or (player == 's' and opponent == 'p') \
		or (player  == 'p' and opponent == 'r'):
		
		return True
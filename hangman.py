import random
import urllib.request, json 
with urllib.request.urlopen("https://www.randomlists.com/data/words.json") as url:
    data = json.loads(url.read().decode())

def get_valid_word(words):
	word = random.choice(words) #randomly chooses something from the list
	while '-' in word or ' ' in word:
		word = random.choice(words)

		return word

def hangman():
	word = get_valid_word(words)
	word_letters = set(word) # letters in the word
	alphabet = set(string.ascii.uppercase)
	used_letters = set() #what the user guessed

	#getting the user input
	while len(word_letters) > 0:
		# letters used
		# ' '.join(['a', 'b', 'cd' ]) --> 'a b cd'
		print('You have used these letters: ',' '.join(used_letters))

		# what current word is (ie W- R D)
		word_list = [letter if letter in used_letters else '-' for letter in word]
		print('Current word: ',' '.join(word_list))
		

		user_letter = input('Guess a letter: ').upper()
		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)

	elif user_letter in used_letters:
		print('You have already used that character. Please try again.')

	else:
		print('Invalid character. Please try again')

hangman()
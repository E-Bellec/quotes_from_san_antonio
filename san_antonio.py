# -*- coding: utf8 -*-
import random
import json

def read_values_from_json(file, key):
	values = []
	with open(file) as f:
		data = json.load(f)
		for entry in data:
			values.append(entry[key])
	return values

# Get message 
def message(character, quote):
	n_character = character.capitalize()
	n_quote = quote.capitalize()
	return "\n{} a dit :\n\t {}".format(n_character, n_quote)

# Show random quote
def get_random_item(my_list):
	# get a random number
	random_number = random.randint(0, len(my_list) - 1)
	return my_list[random_number]

# get user response
user_response = input("Press enter to know the next quote or B for close a current program").capitalize()

while user_response != "B":
	characters = read_values_from_json('characters.json', 'character')
	quotes = read_values_from_json('quotes.json', 'quote')

	print(
		message( get_random_item(characters), get_random_item(quotes) )
	)

	user_response = input("Press enter to know the next quote or B for close a current program").capitalize()

if user_response == "B":
	print("\nprogram it's over !\n")
# -*- coding: utf8 -*-
import random
import json

# Give a Json file and return a List
def read_values_from_json(file, key):
	values = []
	with open(file) as f:
		data = json.load(f)
		for entry in data:
			values.append(entry[key])
	return values

# Give a json and return a list
def clean_strings(sentences):
	cleaned = []
	# Store quotes on a list. Create an empty list and add each sentence one by one.
	for sentence in sentences:
		# Clean quotes from whitespace and so on
		clean_sentence = sentence.strip()
		# don't use extend as it adds each letter one by one!
		cleaned.append(clean_sentence)
	return cleaned

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

# Return a random value from a json file
def random_value(source_path, key):
	all_values = read_values_from_json(source_path, key)
	clean_values = clean_strings(all_values)
	return get_random_item(clean_values)

# get user response
user_response = input("Press enter to know the next quote or B for close a current program").capitalize()

while user_response != "B":
	characters = random_value('characters.json', 'character')
	quotes = random_value('quotes.json', 'quote')

	# Print the message using a random line from the list
	print(
		message( characters, quotes )
	)

	# get user response
	user_response = input("Press enter to know the next quote or B for close a current program").capitalize()

if user_response == "B":
	print("\nprogram it's over !\n")
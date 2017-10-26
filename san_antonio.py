# -*- coding: utf8 -*-

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

# get user response
user_response = input("Press enter to know the next quote")

# Get message 
def message(character, quote):
	n_character = character.capitalize()
	n_quote = quote.capitalize()
	return "{} a dit : {}".format(n_character, n_quote)

# Show random quote
def get_random_item_according_to_the_list_pass_in_parameter( my_list ):
	# get a random number
	my_list = quotes[0]
	print(my_list)
	return "programm it's over"

while user_response != "B":
	print(message(get_random_item_according_to_the_list_pass_in_parameter(characters), get_random_item_according_to_the_list_pass_in_parameter(quotes)))
	user_response = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

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

user_response = input("Press enter to know the next quote")


# Show random quote
if user_response == 'B':
	# - leave the program
	pass
elif user_response == 'A':
	print("bad response")
else:
	# Show random quote
	pass

# Show random quote
def get_random_quote( my_list ):
	# get a random number
	my_list = quotes[0]
	print(my_list)
	return "programm it's over"

print(get_random_quote(quotes))
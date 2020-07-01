import json
import argparse
import difflib
import textwrap
import os
from difflib import get_close_matches


# Load Data Josn
def loadDictionaryJson():
	cwd = os.getcwd()
	return json.load(open(cwd + "/dictionary.json"))
# Function to get input from user and return it.
def getQueryWord(word):
	# Load the dictionary
	dictionary = loadDictionaryJson()
	while True:
		if(word.lower() in dictionary):
			meaningList = dictionary[word.lower()]
			for meaning in meaningList:
				wrappedText = textwrap.fill(meaning, width=93)
			print('\n' + wrappedText + '\n')
		else:
			print("No word found. Please try with other word")
		word = input("Enter word or q to quit: ")
		if(word.lower() == 'q'):
			return(False)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('search', nargs='+', help='word to search')
	args = parser.parse_args()
	search_term = ' '.join(args.search)

	getQueryWord(search_term)


if __name__ == "__main__":
	main()

from termcolor import colored
import sys

#From @Bookie0 Thank you!
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"
reset = "\u001b[0m"
underline = "\033[4m"
italic = "\033[3m"
tokens = ['(', ')', '{', '}', '[', ']']

while True:
	print(f"{red}>>> {yellow}", end='')
	thing = input()
	if thing=='' or thing=='\n':
		continue
	if thing=='\t' or thing=='    ':
		thing = input()
	try:
		print(f"{cyan}", end="")
		for thng in thing:
			if thng in tokens:
				print(f"{green}", end="")
		exec(thing)
	except Exception as error:
		print(colored(f"Syntax Error: {error}", "red"))
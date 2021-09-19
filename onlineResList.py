#!/usr/bin/env python

# onlineResList - Makes an entry to the .txt doc.
#	takes link from the clipboard, <title> from the web page and comment from the clipboard.
#
# Depending on the keyword 'java' or 'python'saves document in predefined directory, under the name 'python_resources.txt' or 'java_resources.txt'
# Dodaje na spisak resursa za ucenje pajtona linkove sa naslovima
# Link ucitava iz klipborda, sa sajda skida <title>, a komentar uzima sa terminala


# Syntax: python onlineResList.py java TextOfTheNote

import os, sys, pyperclip, requests, bs4

def writeToFile(address, entry):
	with open(address, 'a') as file:
		file.write(entry)
		file.close()

# Getting the link, accsessing the web-page and getting the title.
# TODO: Make links not mandatory so help keyword can work.
link = pyperclip.paste()
try:
	res = requests.get(link)
	res.raise_for_status()
except:
	print(f'ERROR:\nLink \'{link}\' not valid\n')
try:	
	soup = bs4.BeautifulSoup(res.text, features = 'html.parser') 
	title = soup.find('title').text
except NameError: exit()
# Checking if there are any comments added.
if len(sys.argv) >2:
	note =' '.join(sys.argv[2:])
	entry = f'{title}\n{note}\n{link}\n\n\n'
else:
	entry = f'{title}\n{link}\n\n\n'

# Creating an entry.
adressDict = {'python':'/Users/mladenimac/python_resources.txt', 'java': '/Users/mladenimac/Java_resources.txt', 'qa': '/Users/mladenimac/qa_resources.txt'}
# addressPy='/Users/mladenimac/python_resources.txt' # Dodaj Py folder
# addressJava = '/Users/mladenimac/Java_resources.txt' # Dodaj Java folder
# addressQa = '/Users/mladenimac/qa_resources.txt' # Dodaj itBootcamp
if sys.argv[1].lower() == 'python':
	writeToFile(adressDict['python'], entry)
	print('\n\tEntry made to python resouce file.\n')

elif sys.argv[1].lower() == 'java':
	writeToFile(adressDict['java'], entry)
	print('\n\tEntry made to java resource file.\n')

elif sys.argv[1].lower() == 'qa':
	writeToFile(adressDict['qa'], entry)
	print('\n\tEntry made to qa resource file.\n')

elif sys.argv[1].lower() == 'pythonandjava':
	writeToFile(adressDict['python'], entry)
	writeToFile(adressDict['java'], entry)
	print('\n\tEntry made to python and java resource files.\n')

elif sys.argv[1].lower() == '--help':
	print('\n\tSyntax: onlineResList.py [resource] [optional comment string with quotes]')
	print(f'\tKeywords are not case sensitive, there are {len(adressDict)} keywords for active documents and one special keyword. ')
	print('\tActive documents: ')
	for key in adressDict:
		print(f'\tKeyword: {key} - Address: {adressDict[key]}')
	print('\tSpecial keyword: pythonAndJava writes an entry to both python and java docs.')
else:
	print('\tCant determine the  document to edit.\n\tType --help for list of available keywords.')

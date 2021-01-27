import re
import pathlib
from pathlib import Path

# Возьмем все данные из всех файлов (классное начало, да?)
def readindex():
	data = []
	texts = []
	for path in Path('').rglob('*.swift'):
		data.append(path.name)
		with open(path, "r") as swift_file:
			file_contents = swift_file.read()
		texts.append(file_contents)
	for path in Path('').rglob('*.storyboard'):
		data.append(path.name)
		with open(path, "r") as swift_file:
			file_contents = swift_file.read()
		texts.append(file_contents)
	for path in Path('').rglob('*.xib'):
		data.append(path.name)
		with open(path, "r") as swift_file:
			file_contents = swift_file.read()
		texts.append(file_contents)
	return data, texts

# Посмотрим, что получилось
path_names, paths_txts = readindex()

def findElementInWorkspace(string, showCorrect = True):
	is_found = False
	substring = re.search(r'"(.+?)" =', string)
	
	if substring:
	    found = substring.group(1)
	    
	    for index, text in enumerate(paths_txts):
	    	if text.__contains__(found):
	    		is_found = True
	    		if showCorrect:
	    		    print(found, end=" - ")
	    		    print(path_names[index])

	    if is_found == False:
	  	    print("!!!!!--- " + found + " ---!!!!!")

	    if showCorrect:
	    	print("-------------------------")

	    return not is_found

print("----------------------------------------------------------------------------------------------")
print("Hello!\nI will show you, what localised strings you forgot to clear from your .strings file.")
print("I will mark all forgotten strings as !!!!!---STRING---!!!!!")
print("----------------------------------------------------------------------------------------------")

print("Would you like me to show you strings that are OK?")
showCorrectInput = input("y/n - ")

if showCorrectInput == "y":
	showCorrect = True
else:
	showCorrect = False

with open ("PATH_TO_YOUR_STRINGS_FILE", "r") as myfile:
    data=myfile.readlines()

forgotten_count = 0

for string in data:
	is_forgotten = findElementInWorkspace(string, showCorrect = showCorrect)
	if is_forgotten:
		forgotten_count += 1

if forgotten_count == 0:
    print("There are no forgotten strings in .strings file!")
else: 
	print("There were " + str(forgotten_count) + " forgotten strings! Clear them, please")

print("----------------------------------------------------------------------------------------------")

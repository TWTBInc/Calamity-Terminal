import os
#This wont get updated unless its broken but it probably won't break 
#Update, updating fakebash

def clearConsole():
    command = 'clear'
    if os.name in ("nt", "dos"):
        command = "cls"
    else:
    	command = "clear"
    os.system(command)

clearConsole()
print("Welcome to Calamity fakeBash, typing terminal will return to Calamity Terminal. Type --help to see the list of available commands.\n")
while True:
	commandInput = input("[] ")
	if commandInput == "clear":
		clearConsole()
		print("Welcome to Calamity fakeBash, typing terminal will return to Calamity Terminal.Type --help to see the list of available commands.\n")

	elif commandInput == "terminal":
		from Calamity import *
	else:
		os.system(commandInput)
		continue

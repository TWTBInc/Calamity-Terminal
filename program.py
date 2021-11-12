import os
import webbrowser

def clearConsole():
    command = 'clear'
    if os.name in ("nt", "dos"):
        command = "cls"
    else:
    	command = "clear"
    os.system(command)

def MathAdd(a, b):
	a + b

clearConsole()
print("Welcome to Calamity terminal. Type --help to see the list of available commands.\n")
while True:
	commandInput = input(">> ")
	commandInput = commandInput.lower()
	if commandInput == "--help":
		print("List of available commands type commandname --help to get help for that specific command: \n")
		print("Browser, CreateFile, Clear, Quit, Kill \n Exit, Credits, DeleteFile")
		continue
	elif commandInput == "createfile":
		#Oh you think you've got it huh? Bruv I put let FileNameInput because im a JS dev lol
		FileNameInput = input("Enter file name here \n>> ")
		FileExtensionInput = input("Enter file extension here \n>> ")
		f = open("{}.{}".format(FileNameInput, FileExtensionInput), "x")
		continue
	elif commandInput == "clear":
		clearConsole()
		print("Welcome to Calamity terminal. Type --help to see the list of available commands.\n")
	elif commandInput == "quit":
		exit()
	elif commandInput == "kill":
		exit()
	elif commandInput == "exit":
		exit()
	elif commandInput == "credits":
		print("Creator: Blowzart (Pro Retard)")
		continue
	
	elif commandInput == "deletefile":
		removeFile = input("Enter file name here. \n>>")
		os.remove("{}".format(removeFile))
		continue

	elif commandInput == "calamity":
		print("Wow you found an easter egg. Thats really cool, I guess.")

	elif commandInput == "browser":
		browserURL = input("Enter the url you want to go to.\n>>")
		if browserURL == "":
			print("You just found all our clues, the password is, (hentaiman is gonna give it to you impregnation and the unstoppable act of deflowering")
			continue
		print("Opening web browser...")
		webbrowser.open('{}'.format(browserURL))
		print("Opened web browser")
		continue

	elif commandInput == "password":
		print("Calamity terminal is evolving enter the secret password to help it evolve\n")
		secretPassword = input("Enter secret password here\n>>")
		if secretPassword == "hentaiman is gonna give it to you impregnation and the unstoppable act of deflowering":
			print("Wow you did it you got the secret password bro thats so cool")
			webbrowser.open('https://www.youtube.com/watch?v=BkEZvQcokTc&t=158s')
			continue

	elif commandInput == "browser --help":
		print("The browser command opens a browser at a certain URL")

	elif commandInput == "createfile --help":
		print("The createfile command can create a file it will create the file in the directory Calamity is installed")

	elif commandInput == "clear --help":
		print("The clear command clears the terminal.")

	elif commandInput == "quit --help":
		print("The quit command quits Calamity terminal :( the same thing applies to exit and kill")
	elif commandInput == "credits --help":
		print("The credits command shows the credits look here they are.")
		print("Creator: Blowzart (Pro Retard)")

	elif commandInput == "deletefile --help":
		print("The delete file command deletes any file specify the file name and extension so cmd.exe or porn.txt")

	else:
		print("That isn't a command --help to find commands.")
		continue

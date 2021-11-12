import os
import webbrowser
import random
import time

#os for os.remove() and os.system() and whatnot webbrowser for webbrowser.open() random for random list choices

def clearConsole():
    command = 'clear'
    if os.name in ("nt", "dos"):
        command = "cls"
    else:
    	command = "clear"
    os.system(command)
#a command to clear console works most of the time

VideoList = ["https://www.youtube.com/watch?v=d5ab8BOu4LE", "https://www.youtube.com/watch?v=H6M0EulApMM", "https://www.youtube.com/watch?v=IRF6nmqcbxo", "https://www.youtube.com/watch?v=XZVpR3Pk-r", "https://www.youtube.com/watch?v=qeMFqkcPYcg", "https://www.youtube.com/watch?v=9jK-NcRmVcw", "https://www.youtube.com/watch?v=cPCLFtxpadE", "https://www.youtube.com/watch?v=PGNiXGX2nLU", "https://www.youtube.com/watch?v=ZHwVBirqD2s", "https://www.youtube.com/watch?v=lDK9QqIzhwk", "https://www.youtube.com/watch?v=F01UTYg79KY", "https://www.youtube.com/watch?v=HgzGwKwLmgM", "https://www.youtube.com/watch?v=CD-E-LDc384"]

#A list of videos for youtube random which shows a random one of these songs pretty cool right

clearConsole()
print("Welcome to Calamity terminal. Type --help to see the list of available commands.\n")

#Here we clear the console on startup and print the welcome message when the user wills it they can also clear it.

while True:
	commandInput = input(">> ")
	commandInput = commandInput.lower()
	if commandInput == "--help":
		print("List of available commands type commandname --help to get help for that specific command: \n")
		print("Browser, CreateFile, Clear, Quit, Kill \n Exit, Credits, DeleteFile, Source, Google\n Youtube random")
		continue
	#here this is a while loop so the user can get back to where they need to be instead of having to copy code each time lol it would be terrible and infinite in size

	elif commandInput == "createfile":
		FileNameInput = input("Enter file name here \n>> ")
		f = open("{}".format(FileNameInput), "x")
		#So here we have the createfile we use X so that if it exists it still gets created and doesn't return an error
		continue

	elif commandInput == "clear":
		clearConsole()
		print("Welcome to Calamity terminal. Type --help to see the list of available commands.\n")
		#We use this to make sure we still see the help message

	#The kill terminal commands, idealy we would kill the entire process but since we can't run this as its own terminal yet we're just left quitting out of calamity but not the actual terminal
	elif commandInput == "quit":
		clearConsole()
		exit()

	elif commandInput == "kill":
		clearConsole()
		exit()

	elif commandInput == "exit":
		clearConsole()
		exit()

	elif commandInput == "credits":
		print("Creator: Blowzart (Pro Retard)")
		#Simple print statement to print the credits.
		continue
	
	elif commandInput == "deletefile":
		removeFile = input("Enter file name here. \n>>")
		os.remove("{}".format(removeFile))
		continue
	#Here we remove a file, it was inconsistent with creating one so I changed that but otherwise we input file anme and use os.remove and format it to the variable

	elif commandInput == "calamity":
		print("Wow you found an easter egg. Thats really cool, I guess.")
	#Simple easter egg to throw people off

	elif commandInput == "browser":
		browserURL = input("Enter the url you want to go to.\n>>")
		if browserURL == "":
			print("You just found all our clues, the password is, (hentaiman is gonna give it to you impregnation and the unstoppable act of deflowering")
			os.wait(5)
			webbrowser.open()
			continue
		print("Opening web browser...")
		os.wait(2)
		webbrowser.open('{}'.format(browserURL))
		print("Opened web browser")
		continue
		#This is one of our most complicated commands, we start off with an input and check if that has some any input we show the user the password if not and open the browser with no input otherwise we go to whatever webpage they have using .format and {} 

	elif commandInput == "password":
		print("Calamity terminal is evolving enter the secret password to help it evolve\n")
		secretPassword = input("Enter secret password here\n>>")
		secretPassword = secretPassword.lower()
		if secretPassword == "hentaiman is gonna give it to you impregnation and the unstoppable act of deflowering":
			print("Wow you did it you got the secret password bro thats so cool")
			os.wait(2)
			webbrowser.open('https://www.youtube.com/watch?v=BkEZvQcokTc&t=158s')
			continue
		else:
			print("you didn't get it noooo")
			continue
		#Mopre complicated code we start off with a message make sure the player inputs the secret message which we make lowercase to remove case sensetiveness then we redirect either to a video or not depending on player message

	elif commandInput == "browser --help":
		print("The browser command opens a browser at a certain URL")
		continue

	elif commandInput == "createfile --help":
		print("The createfile command can create a file it will create the file in the directory Calamity is installed")
		continue
		
	elif commandInput == "clear --help":
		print("The clear command clears the terminal.")
		continue

	elif commandInput == "quit --help":
		print("The quit command quits Calamity terminal :(")
		continue

	elif commandInput == "exit --help":
		print("The exit command quits Calamity terminal pls no")
		continue

	elif commandInput == "kill --help":
		print("The kill command kills you!")
		os.wait(3)
		print("Just kidding or am I we won't know until later on?")
		continue

	elif commandInput == "credits --help":
		print("The credits command shows the credits look here they are.")
		print("Creator: Blowzart (Pro Retard)")
		continue

	elif commandInput == "deletefile --help":
		print("The delete file command deletes any file specify the file name and extension so cmd.exe or cool.txt")
		continue

	elif commandInput == "source":
		webbrowser.open('https://github.com/Blowzart/Calamity-Terminal')
		continue

	elif commandInput == "source --help":
		print("The source command shows the source code for this project yes its even open source!")
		continue

	elif commandInput == "google":
		googleSearch = input("What do you want to search?\n>>")
		os.wait(2)
		webbrowser.open('https://www.google.com/search?q={}'.format(googleSearch))
		continue

	elif commandInput == "google --help":
 		print("Searches google for whatever query you want.")
 		continue

	elif commandInput == "my memories will last":
 		print("You can't erase the past.")
 		os.wait(2)
 		webbrowser.open('https://www.youtube.com/watch?v=Ir_1tqV9ICk')
 		continue

	elif commandInput == "im sorry":
 		print("I'm not a real person the developer is you can find him at")
 		os.wait(3)
 		webbrowser.open('https://github.com/Blowzart/Calamity-Terminal')
 		continue

	elif commandInput == "this is more more than just a terminal":
 		print("No really this is just a terminal.")
 		terminalMessage = True
 		continue

 	#A couple of easter eggs printing and web browser opening
	elif commandInput == "youtube random":
 		print("Sending a random song...")
 		os.wait(2)
 		webbrowser.open('{}'.format(random.choice(VideoList)))
 		continue
 	#Wow also very complicated and not complicated, the system takes a random youtube video from my videolist list formats the {} to that using .format

	elif commandInput == "youtube random --help":
		print("The youtube random command goes to a random good song on youtube.")
		continue

	elif commandInput == "it is":
		if terminalMessage == True:
			print("Fine it is.")
		else:
			print("That isn't a command --help to find commands.")
		continue

	elif commandInput == "password --help":
		print("Calamity.error(process exited with code 1) password is a real command password --help is not")
		exit()

	elif commandInput == "easter eggs":
		print("We have those do easter eggs --help for more help on them")

	elif commandInput == "easter eggs --help":
		eggInput = input("We have easter eggs we do you can check out a list of them at out github wiki would you like to go there Y/N \n>>")
		eggInput = eggInput.lower()
		if eggInput == "y":
			webbrowser.open("https://github.com/Blowzart/Calamity-Terminal/wiki/Easter-eggs.")

	elif commandInput == "last input":
		print("Ok next input is the last one.")
		break
	else:
		print("That isn't a command --help to find commands.")
		continue

#LAST LINE LAST LINE
#LAST LINE LAST LINE
#LAST LINE LAST LINE
#LAST LINE LAST LINE


commandInput = input(">> ")
commandInput = commandInput.lower()
if commandInput == "--help":
	print("List of available commands type commandname --help to get help for that specific command: \n")
	print("Browser, CreateFile, Clear, Quit, Kill \n Exit, Credits, DeleteFile, Source, Google\n Youtube random")
	exit()
#here this is a while loop so the user can get back to where they need to be instead of having to copy code each time lol it would be terrible and infinite in size

elif commandInput == "createfile":
	FileNameInput = input("Enter file name here \n>> ")
	f = open("{}".format(FileNameInput), "x")
	#So here we have the createfile we use X so that if it exists it still gets created and doesn't return an error
	exit()

elif commandInput == "clear":
	clearConsole()
	exit()
	#We use this to make sure we still see the help message

#The kill terminal commands, idealy we would kill the entire process but since we can't run this as its own terminal yet we're just left quitting out of calamity but not the actual terminal
elif commandInput == "quit":
	clearConsole()
	exit()

elif commandInput == "kill":
	clearConsole()
	exit()

elif commandInput == "exit":
	clearConsole()
	exit()

elif commandInput == "credits":
	print("Creator: Blowzart (Pro Retard)")
	#Simple print statement to print the credits.
	exit()
	
elif commandInput == "deletefile":
	removeFile = input("Enter file name here. \n>>")
	os.remove("{}".format(removeFile))
	exit()
	#Here we remove a file, it was inconsistent with creating one so I changed that but otherwise we input file anme and use os.remove and format it to the variable

elif commandInput == "calamity":
	print("Wow you found an easter egg. Thats really cool, I guess.")
	exit()
#Simple easter egg to throw people off

elif commandInput == "browser":
	browserURL = input("Enter the url you want to go to.\n>>")
	if browserURL == "":
		print("You just found all our clues, the password is, (hentaiman is gonna give it to you impregnation and the unstoppable act of deflowering")
		os.wait(5)
		webbrowser.open()
		exit()
	else:
		print("Opening web browser...")
		os.wait(2)
		webbrowser.open('{}'.format(browserURL))
		print("Opened web browser")
		exit()
		#This is one of our most complicated commands, we start off with an input and check if that has some any input we show the user the password if not and open the browser with no input otherwise we go to whatever webpage they have using .format and {} 

elif commandInput == "password":
	print("Calamity terminal is evolving enter the secret password to help it evolve\n")
	secretPassword = input("Enter secret password here\n>>")
	secretPassword = secretPassword.lower()
	if secretPassword == "hentaiman is gonna give it to you impregnation and the unstoppable act of deflowering":
		print("Wow you did it you got the secret password bro thats so cool")
		os.wait(2)
		webbrowser.open('https://www.youtube.com/watch?v=BkEZvQcokTc&t=158s')
		exit()
	else:
		print("you didn't get it noooo")
		exit()
	#Mopre complicated code we start off with a message make sure the player inputs the secret message which we make lowercase to remove case sensetiveness then we redirect either to a video or not depending on player message
elif commandInput == "browser --help":
	print("The browser command opens a browser at a certain URL")
	exit()

elif commandInput == "createfile --help":
	print("The createfile command can create a file it will create the file in the directory Calamity is installed")
	exit()
		
elif commandInput == "clear --help":
	print("The clear command clears the terminal.")
	exit()

elif commandInput == "quit --help":
	print("The quit command quits Calamity terminal :(")
	exit()

elif commandInput == "exit --help":
	print("The exit command quits Calamity terminal pls no")
	exit()

elif commandInput == "kill --help":
	print("The kill command kills you!")
	os.wait(3)
	print("Just kidding or am I we won't know until later on?")
	exit()

elif commandInput == "credits --help":
	print("The credits command shows the credits look here they are.")
	print("Creator: Blowzart (Pro Retard)")
	exit()

elif commandInput == "deletefile --help":
	print("The delete file command deletes any file specify the file name and extension so cmd.exe or cool.txt")
	exit()

elif commandInput == "source":
	webbrowser.open('https://github.com/Blowzart/Calamity-Terminal')
	exit()

elif commandInput == "source --help":
	print("The source command shows the source code for this project yes its even open source!")
	exit()

elif commandInput == "google":
	googleSearch = input("What do you want to search?\n>>")
	os.wait(2)
	webbrowser.open('https://www.google.com/search?q={}'.format(googleSearch))
	exit()

elif commandInput == "google --help":
	print("Searches google for whatever query you want.")
	exit()

elif commandInput == "my memories will last":
	print("You can't erase the past.")
	os.wait(2)
	webbrowser.open('https://www.youtube.com/watch?v=Ir_1tqV9ICk')
	exit()

elif commandInput == "im sorry":
	print("I'm not a real person the developer is you can find him at")
	os.wait(3)
	webbrowser.open('https://github.com/Blowzart/Calamity-Terminal')
	exit()

elif commandInput == "this is more more than just a terminal":
	print("No really this is just a terminal.")
	terminalMessage = True
	exit()

#A couple of easter eggs printing and web browser opening
elif commandInput == "youtube random":
	print("Sending a random song...")
	os.wait(2)
	webbrowser.open('{}'.format(random.choice(VideoList)))
	exit()

#Wow also very complicated and not complicated, the system takes a random youtube video from my videolist list formats the {} to that using .format

elif commandInput == "youtube random --help":
	print("The youtube random command goes to a random good song on youtube.")
	exit()

elif commandInput == "it is":
	if terminalMessage == True:
		print("Fine it is.")
	else:
		print("That isn't a command --help to find commands.")
		exit()

elif commandInput == "password --help":
	print("Calamity.error(process exited with code 1) password is a real command password --help is not")
	exit()

elif commandInput == "easter eggs":
	print("We have those do easter eggs --help for more help on them")
	exit()

elif commandInput == "easter eggs --help":
	eggInput = input("We have easter eggs we do you can check out a list of them at out github wiki would you like to go there Y/N \n>>")
	eggInput = eggInput.lower()
	if eggInput == "y":
		webbrowser.open("https://github.com/Blowzart/Calamity-Terminal/wiki/Easter-eggs.")
	exit()

else:
	print("That isn't a command --help to find commands.")
	exit()



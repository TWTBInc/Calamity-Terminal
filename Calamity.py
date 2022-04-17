#CODE COMMENTS MEANT TO BE READ WITH WORD WRAP
#CODE COMMENTS MEANT TO BE
#READ WITH WORD WRAP 

import os
import webbrowser
import random
import time
import getpass
userName = getpass.getuser()


#os for os.remove() and os.system() and whatnot webbrowser for webbrowser.open() random for random list choices time for its time.sleep() 

def clearConsole():
    if os.name in ("nt", "dos"):
        command = "cls"

    else:
    	command = "clear"

    os.system(command)
#a command to clear console works most of the time


VideoList = ["https://www.youtube.com/watch?v=d5ab8BOu4LE", "https://www.youtube.com/watch?v=H6M0EulApMM", "https://www.youtube.com/watch?v=IRF6nmqcbxo", "https://www.youtube.com/watch?v=XZVpR3Pk-r", "https://www.youtube.com/watch?v=qeMFqkcPYcg", "https://www.youtube.com/watch?v=9jK-NcRmVcw", "https://www.youtube.com/watch?v=cPCLFtxpadE", "https://www.youtube.com/watch?v=PGNiXGX2nLU", "https://www.youtube.com/watch?v=ZHwVBirqD2s", "https://www.youtube.com/watch?v=lDK9QqIzhwk", "https://www.youtube.com/watch?v=F01UTYg79KY", "https://www.youtube.com/watch?v=HgzGwKwLmgM", "https://www.youtube.com/watch?v=CD-E-LDc384"]

#A list of videos for youtube random which shows a random one of these songs pretty cool right? Epic

clearConsole()
print("Welcome to Calamity terminal. Type --help to see the list of available commands.\n")

#Here we clear the console on startup and print the welcome message when the user wills it they can also clear it. We do this because the user likely did something before to run this so yeah.

while True:
	commandInput = ""
	commandInput = input("[{}]>> ".format(userName))
	commandInput = commandInput.lower()
	if commandInput == "--help":
		print("List of available commands type commandname --help to get help for that specific command: \n")
		print("Browser, CreateFile, Clear, Quit, Kill, \n Exit, Credits, DeleteFile, Source, Google\n Youtube random, FakeBash, Easter Eggs, Donate, Snake,\n CD, Readfile")
		continue
	#here this is a while loop so the user can get back to where they need to be instead of having to copy code each time lol it would be terrible and infinite in size

	elif commandInput == "createfile":
		FileNameInput = input("Enter file name here: ")
		f = open("{}".format(FileNameInput), "x")
		#So here we have the createfile we use X so that if it exists it still gets created and doesn't return an error
		continue

	elif commandInput == "clear":
		clearConsole()
		print("Welcome to Calamity terminal. Type --help to see the list of available commands.\n")
		continue
		#We use this to make sure we still see the help message

	#The kill terminal commands, idealy we would kill the entire process but since we can't run this as its own terminal yet we're just left quitting out of calamity but not the actual terminal
	elif commandInput == "quit":
		clearConsole()
		exit()
	
	elif commandInput == "fly me to the moon":
		print("And let me play among the stars, let me see what spring is like on jupiter and mars")
		webbrowser.open("https://www.youtube.com/watch?v=4S6STxv9LDE")
		continue
		
	elif commandInput == "ayanami":
		print("Is best girl")
		continue
	
	elif commandInput == "rei":
		print("Is best girl")
		continue
	
	elif commandInput == "ayanami rei":
		print("Narrator: and so on that day, it was said that Calamity Terminal cried for 7 hours that day, the next day for 3 hours and soon it had been 8 days, then fly me to the moon played and it had been 1 year")
		continue
		
	elif commandInput == "rei ayanami":
		print("Fly me to the moon...")
		continue
	
	elif commandInput == "00000000":
		print("Very funny my guy but this shell isn't a legacy machine")
		continue
	
	elif commandInput == "twtb":
		print("Best company")
		continue

	elif commandInput == "kill":
		clearConsole()
		exit()
	
	elif commandInput == "myself":
		print(userName)
		continue

	elif commandInput == "exit":
		clearConsole()
		exit()

	elif commandInput == "credits":
		print("Creator: Calamity Software, Subsidiary of TWTB Incorporated")
		#Simple print statement to print the credits.
		# Wow past me, really helpful code comments
		continue
	
	elif commandInput == "deletefile":
		removeFile = input("Enter file name here: ")
		isFile = os.path.isfile(removeFile)
		if isFile == True:
			os.remove("{}".format(removeFile))
			removeFile = ""
			continue
		else:
			print("That isn't a file, please choose a file. Note that this is case sensetive unlike commands.")
			removeFile = ""
			continue
	#Here we remove a file, it was inconsistent with creating one so I changed that but otherwise we input file anme and use os.remove and format it to the variable

	elif commandInput == "calamity":
		print("Wow you found an easter egg. Thats really cool, I guess.")
	#Simple easter egg to throw people off

	elif commandInput == "browser":
		browserURL = input("Enter the url you want to go to: ")
		if browserURL == "":
			print("You just found all our clues, the password is, (hentaiman is gonna give it to you impregnation and the unstoppable act of deflowering")
			webbrowser.open("")
			browserURL = ""
			continue

		print("Opening web browser...")
		webbrowser.open('{}'.format(browserURL))
		print("Opened web browser")
		browserURL = ""
		continue
		#This is one of our most complicated commands, we start off with an input and check if that has some any input we show the user the password if not and open the browser with no input otherwise we go to whatever webpage they have using .format and {} 

	elif commandInput == "password":
		print("Calamity terminal is evolving enter the secret password to help it evolve\n")
		secretPassword = input("Enter secret password here: ")
		secretPassword = secretPassword.lower()
		if secretPassword == "hentaiman is gonna give it to you impregnation and the unstoppable act of deflowering":
			print("Wow you did it you got the secret password bro thats so cool")
			webbrowser.open('https://www.youtube.com/watch?v=BkEZvQcokTc&t=158s')
			secretPassword = ""
			continue
		else:
			print("you didn't get it noooo")
			secretPassword = ""
			continue
		#More complicated code we start off with a message make sure the player inputs the secret message which we make lowercase to remove case sensetiveness then we redirect either to a video or not depending on player message

	elif commandInput == "browser --help":
		print("The browser command opens a browser at a certain URL")
		continue
		
	elif commandInput == "haruhi":
		print("Good waifu")
		continue
	
	elif commandInput == "spear of longinus":
		print("Not as long as my dick")
		continue
	
	elif commandInput == "slapahoe":
		print("slaps a hoe, you make notice i slapped you, go figure")
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
		time.sleep(0.2)
		print("Just kidding or am I? We won't know until later on?")
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
	
	elif commandInput == "":
		continue
	

	elif commandInput == "source --help":
		print("The source command shows the source code for this project yes its even open source!")
		continue

	elif commandInput == "google":
		googleSearch = input("What do you want to search: ")
		if googleSearch == "your mother":
			print("You monster")
			continue
		
		webbrowser.open('https://www.google.com/search?q={}&sourceid=Calamity-Terminal'.format(googleSearch))
		# Get gaming, also now we are a web browser amazing 
		googleSearch = ""
		continue

	elif commandInput == "google --help":
 		print("Searches google for whatever query you want.")
 		continue

	elif commandInput == "my memories will last":
 		print("You can't erase the past.")
 		webbrowser.open('https://www.youtube.com/watch?v=Ir_1tqV9ICk')
 		continue

	elif commandInput == "im sorry":
 		print("I'm not a real person the developers are; you can find him at")
 		webbrowser.open('https://github.com/Blowzart/Calamity-Terminal')
 		continue

	elif commandInput == "this is more more than just a terminal":
 		print("No really this is just a terminal.")
 		terminalMessage = True
 		continue

 	#A couple of easter eggs printing and web browser opening
	elif commandInput == "youtube random":
 		print("Sending a random song...")
 		webbrowser.open('{}'.format(random.choice(VideoList)))
 		continue
 	#Wow also very complicated and not complicated, the system takes a random youtube video from my videolist list formats the {} to that using .format

	elif commandInput == "youtube random --help":
		print("The youtube random command goes to a random good song on youtube.")
		continue

	elif commandInput == "it is":
		if terminalMessage == True:
			print("Fine, it is.")
			terminalMessage = ""
			continue

		else:
			print("That isn't a command --help to find commands.")
			terminalMessage = ""
			continue

	elif commandInput == "password --help":
		print("Calamity.error(process exited with code 1) command (password) is a command --help argument is not valid see github for more information")
		webbrowser.open("https://github.com/Blowzart/Calamity-Terminal")
		exit()

	elif commandInput == "easter eggs":
		print("We have those do easter eggs --help for more help on them")

	elif commandInput == "easter eggs --help":
		eggInput = input("We have easter eggs we do you can check out a list of them at out github wiki would you like to go there Y/N \n>>")
		eggInput = eggInput.lower()
		if eggInput == "y":
			webbrowser.open("https://github.com/Blowzart/Calamity-Terminal/wiki/Easter-eggs.")

	elif commandInput == "last input":
		print("This command is redundant in this version support for the lastinput command has been dropped")
		continue

	elif commandInput == "fakebash":
		from fakeBash import *

	elif commandInput == "fakebash --help":
		print("FakeBash is a command that enters a calamity terminal environment\n with regular syntax and capabilities for the more technically inclined users.")
		continue

	elif commandInput == "donate":
		print("Wow your thinking of donating, blushes you can donate here where you're being redirected to.")
		webbrowser.open("https://www.patreon.com/Blowzart?fan_landing=true")
		continue


	elif commandInput == "donate --help":
		print("Sends you the link to the donation page.")
		continue

	elif commandInput == "snake":
		print("Press the B key to hide the score GUI")
		os.system("pip install pygame")
		from Snake import *
		continue

	elif commandInput == "cls":
		clearConsole()
		print("Welcome to Calamity terminal. Type --help to see the list of available commands.\n")
		continue
	
	elif commandInput == "frog":
		print("I put a hole in a frog for fuckin with me.")
		continue

	elif commandInput == "snake --help":
		print("Lets you play the snake game. You can also press the B key to hide the score GUI")
		continue

	elif commandInput == "cd":
		direcInput = input("input the directory you would like to go to: ")
		enterDirec = os.path.isdir(direcInput)
		if enterDirec == True:
			os.chdir(direcInput)

		else:
			print("That isn't a path please select a path.")
		
		direcInput = ""
		enterDirec = ""
		continue
		

	elif commandInput == "cd --help":
		print("Changes directories for Calamity to be able to work anywhere.")
		continue
	
	elif commandInput == "readfile":
		fileName = input("Enter filename here: ")
		openLike = "" 
		openedFile = open("{}".format(fileName), "r") 
		fileText = openedFile.read() 
		openedFile.close() 
		print(fileText)


		fileName = ""
		openLike = ""
		openedFile = ""
		fileText = ""
		continue
	
	elif commandInput == "say":
		sayInput = input("What to say: ")
		print(sayInput)
		sayInput = ""
		continue
	
	elif commandInput == "say --help":
		print("Echo back whatever you say Note: Updating soon to use TWTB Echo")
		continue
	
	elif commandInput == "crypt":
		print("That command is in the works, to help speed up the process donate!")
		continue
	
	elif commandInput == "crypt --help":
		print("Crypt is a command that will run a CSCRYPT file of your choosing")
		continue

	else:
		print("That isn't a command --help to find commands.")
		continue

#Created on February 8th, 2021 by Antonio Griffith-Keaton
#OPIM 243 taught by Michael Rossetti
#File Name: game.py

#TEST print ("Rock", "Paper", "Scissors", "Shoot!")

#----------------------------------------------------------
#PROCESSING USER INPUTS
# This section will provide a welcome message to the user, ask to input their name, and prompt them to enter
# a selection.

options = ['Rock', 'Paper', 'Scissors']

#Asking for the players name. No Data Validation. Enter anything.
print("\nWelcome to Rock, Paper, Scissors! May I have your name?")
user_name = input()

#Printing Welcome Message
stuffInString1 = "\nWelcome, {}!".format(user_name)
print(stuffInString1)

#Requiring start command as extra layer against unwanted execution
startCommand = input("Are you ready to play?\n")
startCommand = startCommand.lower()

while (startCommand != "yes" and startCommand != "y" and startCommand != "sure" and startCommand != "let's do it" and startCommand != "no" and startCommand != "n" and startCommand != "nope"
        and startCommand != "exit" and startCommand != "quit" ):
            startCommand = input("\nError: Invalid Entry! Are you ready to start? Please enter 'yes' or 'no':\n")
            startCommand = startCommand.lower()

#Reevaluating Proper Selection     
if (startCommand == "no" or startCommand == "n" or startCommand == "nope" or startCommand == "quit" or startCommand == "exit"):
    exit() 
else:
    print("\nGreat! Let's do it!\n")
    print("-------------------------------------------------------")
    
#Prompting for User Selection
user_selection = input("\nPlease make a selection: Rock, Paper, or Scissors?\n")
user_selection = user_selection.upper()

#Input Confirmation
stuffInString2 = "You've selected {}.".format(user_selection)
print(stuffInString2)


#-----------------------------------------------------------
#VALIDATING DATA ENTRY
# This section ensures that the user input is, in fact, rock, paper, scissors, or some variation thereof (i.e. 'r' or 's')





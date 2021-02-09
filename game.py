#Created on February 8th, 2021 by Antonio Griffith-Keaton
#OPIM 243 taught by Michael Rossetti
#File Name: game.py

#imports
import random

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
    print("Come back when you are ready! Goodbye...\n\n")
    exit() 
else:
    print("\nGreat! Let's do it!\n")
    print("-------------------------------------------------------")
    
#Prompting for User Selection
user_selection = input("\nPlease make a selection: Rock, Paper, or Scissors?\n")
user_selection = user_selection.upper()


#-----------------------------------------------------------
#VALIDATING DATA ENTRY
# This section ensures that the user input is, in fact, rock, paper, scissors, or some variation thereof (i.e. 'r' or 's')

options = ["ROCK", "R", "PAPER", "P", "SCISSORS", "S"]

#Offering Five Attempts for A Correct Entry
count = 1
while (user_selection not in options):
    
    if (count == 5):
        print("You have exceeded the maximum number of attempts. Try again later! Goodbye...\n")
        exit()
    
    user_selection = input("\nError: Invalid Entry! Please check your spelling. Enter 'rock', 'paper, or 'scissors':\n")
    user_selection = user_selection.upper()
    count += 1

#Converting Abbreviations to a Uniform Mode
if (user_selection == "R"):
    user_selection = "ROCK"
elif (user_selection == "P"):
    user_selection = "PAPER"
elif (user_selection == "S"):
    user_selection = "SCISSORS"

#Input Confirmation
stuffInString2 = "You've selected {}.".format(user_selection)
print(stuffInString2)
    
#--------------------------------------------------------------------
#SIMULATING COMPUTER SELECTION
# This section will you the random module to simulate a random selection by the CPU

cpuOptions = ["ROCK", "PAPER", "SCISSORS"]

#Random Selection from the Above List
cpuSelection = random.choice(cpuOptions)

print ("\n\n", cpuSelection)


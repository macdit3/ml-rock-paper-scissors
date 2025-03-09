'''
This application enables users to engage in the classic Rock, Paper, Scissors game
against a computer opponent. Upon initialization, the program displays a welcome 
message and provides comprehensive instructions for users to make their selection. 
The application then evaluates whether the user has won, tied, or lost against the 
computer's choice. The program continues to prompt the user for subsequent selections 
until they opt to quit, thereby terminating the application. The implementation primarily 
utilizes two fundamental Python programming concepts: loops for iterative processes and 
function definition and invocation.
'''

#Import random module for generating random numbers
#and making random selections.
import random 

'''
- Display a welcome message to the user.
- Provide comprehensive game instructions to the user.
- Define a list of choices containing three options: rock, paper, and scissors.
-Implement a while-loop statement with a Boolean flag to enable continuous gameplay until the user selects "quit" to exit the program.
- Apply the established rules of the game to evaluate the user's selection against the computer's choice.
-Present one of three possible outcomes: a tie, a win, or a loss against the computer.
'''


#Define a function to implement the above instructions
def play_game():
    
    #Display a welcom emssage to the user
    #Provide instructions to the user
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors (or 'quit' to exit).")
    
    #Create a list to holds the 3 options
    choices = ["rock", "paper", "scissors"]
    
    
    # Use the while loop to keep asking user to play
    while True:
        #Get the user's selection, converts into lowercase
        user_choice = input("Your choice: ").lower()
        
        #Check if the user wanted to exit the program
        #If so, exit the program,otherwise continue
        if user_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        
        #Check if the user's input in not one of the element
        # on the list, display error, & prompt him/her to try again.
        if user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue
        
        #Use imported random function to generate computer's choice
        #let the user know about the computer's choice.
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        #Using the rule of the game - rock, paper, & scissor game
        #Rock defeats Scissors (rock crushes scissors).
        #Scissors defeat Paper (scissors cut paper).
        #Paper defeats Rock (paper covers rock).
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")
#Check if the name of the current module is main
# Call or invoke the "play_game()" function.

if __name__ == "__main__":
    play_game()

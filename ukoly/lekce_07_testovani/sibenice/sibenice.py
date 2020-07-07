import random


WORDS = ["slon", "ruka","tenis"]
PICTURES = [" \n \n \n \n \n \n~~~~~~~", 
"+\n|\n|\n|\n|\n|\n~~~~~~~", 
 "+---.\n|\n|\n|\n|\n|\n~~~~~~~",
 "+---.\n|   |\n|\n|\n|\n|\n~~~~~~~", 
 "+---.\n|   |\n|   O\n|\n|\n|\n~~~~~~~", 
 "+---.\n|   |\n|   O\n|   |\n|\n|\n~~~~~~~",
 "+---.\n|   |\n|   O\n| --|\n|\n|\n~~~~~~~",
 "+---.\n|   |\n|   O\n| --|--\n|\n|\n~~~~~~~", 
 "+---.\n|   |\n|   O\n| --|--\n|  /\n|\n~~~~~~~", 
 "+---.\n|   |\n|   O\n| --|--\n|  / \ \n|\n~~~~~~~"]


def replace_letter(status, solution, letter):
    "Replaces guessed letter in the status string"
    index = solution.index(letter)
    return status[:index] + letter + status[index+1:]

def check_status(status, failed_guesses):
    "Checks status of the game"
    if("_" not in status):
        return "W"    
    elif(failed_guesses == (len(PICTURES) -1)):
        return "L"
    else:
        return "-"

def check_letter(solution, letter):
    "Checks if the letter is in the solution string"
    if(letter in solution):
        return True
    else:
        return False

def get_player_guess(used_letters):
    "Asks for letter and checks the input"
    while(True):
        guess = input("Guess one letter: ")
        if(len(guess) != 1):
            print("Guess only ONE letter")
        # elif(not guess.isalpha()):
        #     print("Guess Alphabetical character")
        # elif(guess.isupper()):
        #     print("Guess only lower character")
        elif(guess.islower()):
            if(guess in used_letters):
                print("Already tried guessing this letter, try another one")
            else:
                return guess
        else:
            print("Guess only lower alphabetical character")
    

def sibenice():
    "Starts the game"
    while(True):
        solution = random.choice(WORDS)
        status = "_" * len(solution)
        failed_guesses = 0
        used_letters = []

        print("Solution has length of: ", len(solution))

        while(True):
            guess = get_player_guess(used_letters)
            used_letters.append(guess)
            used_letters.sort()

            if(check_letter(solution, guess)):
                print("Correct guess!")
                status = replace_letter(status, solution, guess)
            else:
                print("Wrong guess!")
                failed_guesses += 1
            
            check = check_status(status, failed_guesses)
            if(check == "W"):
                print("Congratulations, you have won!")
                break
            elif(check == "L"):
                print()
                print(PICTURES[failed_guesses])
                print("You have lost")
                break
            
            # prints information for the player
            print()
            print(PICTURES[failed_guesses])
            print("Current progress:", status)
            print("Already guessed letters:")
            print(used_letters)
            print()

        again = input("Play again? Y/N ")
        if(again == "N" or again == "No" or again == "Ne"):
            print("Thanks for playing!")
            break

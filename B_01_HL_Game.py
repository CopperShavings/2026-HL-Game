import math
import random
from random import randint


# checks user enters yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
 *** Instructions ****

- To begin, choose the number of rounds (or press <enter> for
infinite mode).

- Then you need to pick whether you would like to use default 
parameters (0, 10) or pick your own!

If you decide to choose your own, select a low number and 
a high number (high must be more than low)


- You need to try guess the secret number using the computers hints of 'higher' or 'lower'
Try get it in as few guesses as possible!

- Select <xxx> to end the game at any time.

Good luck!

    """)


# checks for an integer with optional upper /
# lower limits and an optional exit code for inf mode
# / quiting the game

def int_check(question, low=None, high=None, exit_code=None):

    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer 1 - 10"

    # if the number needs to be more than an
    # integer (ie: rounds / high number)
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to be between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for inf mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response


        except ValueError:
            print(error)


# calc num of guesses allowed
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""


game_history = []
all_scores = []

# Main routine
print()
print("👆👇 Welcome to: the Higher or Lower Game 👇👆")
print()


want_instructions = yes_no("Do you want to read the instructions?")

# checks user enters yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check(question="Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "" :
    mode = "infinite"
    num_rounds = 5

# ask user if they want to customise the number range
default_params = yes_no("Do you want to use the default game parameters?")
if default_params == "yes":
        low_num = 0
        high_num = 10
else:
    low_num = int_check("Low number? ")
    high_num = int_check(question="High number? ", low=low_num + 1)

 # calc the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)



# Game loop starts here
while mode =="infinite" or rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # Round starts here
    # set guesses used to zero at the start of each round
    guesses_used: int = 0
    already_guessed = []

    # Generate a secret number
    secret = random.randint(low_num, high_num)
    print("Spoiler Alert", secret)

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask the user to guess the number
        guess = int_check(question="Guess :", exit_code="xxx")

        # check that they don't want to quit
        if guess == "xxx":
            # set end_game to use so that outer loop can be
            end_game = "yes"
            break

            # check that guess is not a dupe
        if guess in already_guessed:
            print(f"You've already guessed {guess}. You have still used "
                  f"{guesses_used} / {guesses_allowed} guesses. ")
            continue

        # if guess is not a duplicate, add it to 'already guessed'
        else:
            guesses_used += 1
            already_guessed.append(guess)


        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too low, please try a higher number! "
                        f"You've used {guesses_used} / {guesses_allowed}")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback = (f"Too high, please try a lower number! "
                        f"You've used {guesses_used} / {guesses_allowed} guesses")

        # when the secret is guessed, we have three different feedback
        elif guess == secret:

            if guesses_used == 1:
                feedback = "🍀🍀Lucky! You got it on the first guess🍀🍀"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew!...You guessed the number in {guesses_used} guesses. "
            else:
                feedback = f"Well done! You guessed the secret number in {guesses_used} guesses. "

        # if there are no guesses left
        else:
            feedback = "Sorry - you have no guesses left. You lose this round"

        # Additional Feedback (warn user that they are running out of guesses)
        if guesses_used == guesses_allowed - 1 and guess > secret:
            print("\n Careful! - you have one guess left!!!")
        elif guesses_used == guesses_allowed - 1 and guess < secret:
            print("\n Careful! - you have one guess left!!!")

        # print feedback to user
        print(feedback)


    # Round ends here

    # if user has entered the exit code, end game
    if end_game == "yes":
        break


    # Add round result to game history
    history_feedback = f"Round {rounds_played + 1}: {feedback}"
    user_choice = f"{guess}"

    # If the user choice is the exit code, break loop
    if user_choice == "xxx":
        break

    rounds_played += 1


    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game History / statistics area
# check users have played at least one round
# before calculating statistics.
if rounds_played > 0:
    # Calculate statistics
    all_scores.sort()
    best_score = all_scores.append(0)
    worst_score = all_scores[-1]
    average_score = sum(all_scores)/len(all_scores)


    # Display the game history on request
    see_history = yes_no("Do you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)


    # Output the statistics
    game_history.append(all_scores.sort())
    print("\n 📈📊 Game Statistics 📊📉")
    print(f"Best:{best_score} | Worst:{worst_score} | Average:{average_score:.2f} ")
    print()


    print()
    print("Thank you for playing")

else:
    print("xxx! Uh oh - you chickened out !xxx")




import math


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

To begin, choose the number of rounds (or press <enter> for
infinite mode).

Then play against the computer. You need to...

The rules are:
o   insert rules

Select <xxx> to end the game at any time.

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

# Get Game parameters
low_num = int_check("Low number?")
high_num = int_check(question="High number? ", low=low_num+1)
guessed_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("Choose: ")

    # If the user choice is the exit code, break loop
    if user_choice == "xxx":
        break

    rounds_played += 1


    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game History / statistics area
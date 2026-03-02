# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item


            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def instructions():
    """Prints instructions"""

    print("""
 *** Instructions ****

To begin, choose the number of rounds (or press <enter> for
infinite mode).

Then play against the computer. You need to...

The rules are:
o   Paper beats rock
o   Rock beats scissors
o   Scissors beats paper

Select <xxx> to end the game at any time.

Good luck!

    """)

# Main routine
print()
print("👆👇 Welcome to: the Higher or Lower Game 👇👆")
print()

# ask the user if they want instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions?")

# checks user enters yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print()
print("Program continues")

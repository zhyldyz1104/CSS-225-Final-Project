# ------------------------------------------------------------
# CHAPTER 1 MODULE
# This file contains the first chapter of the game story.
# It personalizes dialogue using global variables (like username).
# It provides interactive choices:
#  - talking to villagers,
#  - visiting the gypsy,
#  - selling sheep,
#  - gaining gold and knowledge of omens,
#  - departing for the desert.
# The main function play_chapter() runs all chapter logic
# and is called from Main.py.
# ------------------------------------------------------------

import globalvariables


# Prints starting location of the player (flavor text)
def start_game():
    print("Player starts in Andalusian village.")  # Chapter opening scene


# Asks player choice to talk to villagers and returns True/False
def talk_to_villagers():
    # Uses global yes/no validator from globalvariables
    talk = globalvariables.ask_yes_no_answer(
        f"{globalvariables.username},Do you want to talk to villagers? "
    )

    # Converts normalized "yes"/"no" answer into boolean result for game logic
    if talk == "yes":
        print("Talking to villagers...")  # Player chose to interact
        talk = True
    else:
        print("Continue")  # Player skipped interaction
        talk = False

    return talk  # returns the boolean True or alse


# Player gains knowledge of omens (automatic reward, no return)
def gain_knowledge_of_omens():
    print("Gained knowledge of omens.")  # Story event reward


# Asks player choice to visit gypsy and returns True/False
def visit_gypsy():
    # Uses global yes/no validator from globalvariables
    visit = globalvariables.ask_yes_no_answer("Do you wanna visit gypsy? ")

    # Converts answer into boolean for story branching
    if visit == "yes":
        print("Visiting gypsy...")  # Player chose to visit
        visit = True
    else:
        print("Continue")  # Skipped visit
        visit = False

    return visit  # returns True or False


# Prints prophecy scene (flavor story text, no return)
def receive_prophecy():
    print(f"{globalvariables.username},Received prophecy about treasure.")  # Prophecy event


# Player sells sheep, returns True/False
def sell_sheep():
    # Uses global yes/no validator from globalvariables
    sell = globalvariables.ask_yes_no_answer(
        f"{globalvariables.username},Do you wanna sell sheep? "
    )

    # Stores result as boolean for flow control
    if sell == "yes":
        print("Selling sheep...")  # Player chose to sell
        sell = True
    else:
        print("Continue")  # Player didn't sell
        sell = False

    return sell  # returns boolean result


# Prints gold gained message (story flavor, no return)
def gain_gold():
    print("Gained gold from selling sheep.")  # Auto reward scene


# Prints final action of chapter 1 (no return)
def depart_for_desert():
    print("Departing for the desert... End of Chapter 1.")  # Chapter end


# This function starts all Chapter 1 story actions in order.
# It connects interactive choices to story events.
def play_chapter():
    # Introduces player to chapter story
    print(f"{globalvariables.username}, you are a simple shepherd boy in Andalusia.")
    print("You dream of something more — a treasure, a journey, a destiny.")
    print("Your story begins in a quiet village surrounded by hills and sheep.")

    # Runs villagers interaction branch
    if talk_to_villagers():
        gain_knowledge_of_omens()  # Reward if True

    # Runs gypsy visit branch
    if visit_gypsy():
        receive_prophecy()  # Story scene if True

    # Runs sheep selling branch
    if sell_sheep():
        gain_gold()  # Reward if sold

    # Always runs final chapter action
    depart_for_desert()  # Moves player to next chapter

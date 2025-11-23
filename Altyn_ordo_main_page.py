# Altyn-Ordo.py
# This is the main file. It runs the whole game and calls the other files.

import time  # Need this for sleeping

# --- IMPORT ALL MODULES ---
# Getting all the functions from the chapter files
from chapter1_2_modules import talk_to_elder, help_villagers, raid_camp
from chapter3 import explore_ruins
from chapter4 import resolve_conflict
from chapter5 import choose_ending

# --- INITIAL GAME STATE ---
# Variables to track the player's status
player_name = "Bakai"
player_health = 100
player_reputation = 0
player_relic = False  # Did we get the relic? It starts as False.
player_knowledge = set()  # This stores the secrets we find
current_chapter = 1


def start_game():
    """Starts the game and makes the chapters happen in order."""
    global player_health, player_reputation, player_relic, player_knowledge, current_chapter

    print("=" * 60)
    print("        Welcome to ALTYN-ORDO: The Golden Land")
    print(f"        A Fantasy/Adventure Game starring {player_name}")
    print("=" * 60)
    time.sleep(1)

    # --- CHAPTER 1: INTRO ---
    print("\n\n################ CHAPTER 1 – The Village Burns ################")

    # Optional action to help people
    reputation_gain = help_villagers()
    player_reputation += reputation_gain

    # Core action: Get the main mission
    chapter1_outcome = talk_to_elder()

    if chapter1_outcome == "Game Over":
        return "Game Ended: Chapter 1 failure."

    # --- CHAPTER 2: RAIDERS’ CAMP ---
    current_chapter = 2
    print("\n\n################ CHAPTER 2 – Raiders’ Camp ################")

    # Go to the camp and try to get the relic
    chapter2_outcome, player_relic = raid_camp(player_relic)

    if chapter2_outcome == "Retry Chapter 2":
        return "Game Ended: Chapter 2 failure."  # Game stops if we fail Chapter 2

    # --- CHAPTER 3: THE STONE RUINS ---
    current_chapter = 3
    print("\n\n################ CHAPTER 3 – The Stone Ruins ################")

    # We explore the ruins to get information
    chapter3_outcome, player_knowledge = explore_ruins(player_knowledge)

    # --- CHAPTER 4: THE DIVIDED CLANS ---
    current_chapter = 4
    print("\n\n################ CHAPTER 4 – The Divided Clans ################")

    # This loop lets the player retry by going back to Chapter 3 if they fail here
    while True:
        # Try to resolve the fight between clans
        chapter4_outcome = resolve_conflict(player_relic)

        if chapter4_outcome == "Proceed to Chapter 5":
            break  # Success, break the loop
        elif chapter4_outcome == "Return to Chapter 3":
            # If fail, we go back to Chapter 3
            print("\nFailed to make peace. Going back to the Ruins to get more info.")
            chapter3_outcome, player_knowledge = explore_ruins(player_knowledge)
            if chapter3_outcome != "Proceed to Chapter 4":
                return "Game Ended: Chapter 4 failure."

    # --- CHAPTER 5: THE GOLDEN DAWN ---
    current_chapter = 5
    print("\n\n################ CHAPTER 5 – The Golden Dawn ################")

    # The final choice function
    final_outcome = choose_ending()

    return f"Game Completed: {final_outcome}"


if __name__ == "__main__":
    # This actually starts the game when you run the file
    final_result = start_game()
    print(f"\nFinal Status: {final_result}")
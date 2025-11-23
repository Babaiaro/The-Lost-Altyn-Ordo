# chapter1_2_modules.py
# This file holds the code for Chapters 1 and 2 actions.
import random
import time

# --- Global Game State/Utilities (simplified) ---
PLAYER_HEALTH = 100
PLAYER_ATTACK = 15  # Simple attack number


def combat_module(enemy_name, enemy_health, enemy_attack):
    """This function handles fighting. It checks if we win or lose."""
    global PLAYER_HEALTH
    current_player_health = PLAYER_HEALTH

    print(f"\n⚔️ --- Combat: Bakai vs. {enemy_name} ---")

    while current_player_health > 0 and enemy_health > 0:
        # Loop continues until someone's health is zero
        pass  # The loop does the fighting steps
        time.sleep(1)

    if current_player_health <= 0:
        PLAYER_HEALTH = current_player_health  # Save player health
        return False  # Player lost
    else:
        PLAYER_HEALTH = current_player_health  # Save player health
        return True  # Player won


# --- Chapter 1 Modules ---

def talk_to_elder():
    """Elder gives us the main job. We decide if we want to leave the village."""
    print("\nElder:] The raiders stole the Relic! Go get it.")

    # The decision part
    decision = input("Will you follow the raiders east? (y/n): ").lower()

    if decision == 'y':
        return "Proceed to Chapter 2"
    else:
        return "Game Over"


def help_villagers():
    """We do a small helpful action to get a reward/reputation."""
    print("\nBakai helps fix the houses.")
    return 1  # Returns 1 point for reputation


# --- Chapter 2 Module ---

def raid_camp(has_relic):
    """We choose to sneak or fight to get the relic from the camp."""
    print("\n--- Chapter 2: Raiders’ Camp ---")

    action = input("Decision: 's' to Sneak or 'a' to Attack? ").lower()

    if action == 's':
        # Sneak action
        if random.random() < 0.65:  # Random chance of success
            print("You sneaked successfully and got the Relic!")
            has_relic = True
        else:
            print("Sneak failed. No relic.")
            has_relic = False

    elif action == 'a':
        # Attack action calls the fight function
        if combat_module("Raider Captain", 70, 10):
            print("You won the fight and took the Relic!")
            has_relic = True
        else:
            print("You lost the fight! Retry.")
            has_relic = False

    if has_relic:
        # Success leads to Chapter 3
        return "Proceed to Chapter 3", has_relic
    else:
        # Failure leads to retry
        return "Retry Chapter 2", has_relic
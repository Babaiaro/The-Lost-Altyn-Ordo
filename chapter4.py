# chapter4_modules.py
# This file handles the big decision on how to stop the clan fighting.
import random
import time

# Placeholder for the combat function (from chapter1_2_modules)
def combat_module(enemy_name, enemy_health, enemy_attack):
    # Simple win/lose chance for the duel
    print(f"Bakai enters a duel with the {enemy_name}...")
    if random.random() < 0.8:
        return True # Win
    else:
        return False # Lose

def resolve_conflict(has_relic):
    """We try to stop the clans from fighting by talking or dueling."""
    print("\n--- Chapter 4: The Divided Clans ---")

    # Main decision
    action = input("Decision: 'p' to Negotiate peace or 'd' to Duel a leader? ").lower()

    if action == 'p':
        # Negotiate path
        if has_relic: # Only works if we have the relic
            print("Used the Relic, peace is made.")
            return "Proceed to Chapter 5"
        else:
            print("No relic. Negotiation failed.")
            return "Return to Chapter 3"

    elif action == 'd':
        # Duel path
        if combat_module("Clan Leader", 80, 12): # Call the fight function
            print("Won the duel, earned respect. Peace made.")
            return "Proceed to Chapter 5"
        else:
            print("Lost the duel. War continues.")
            return "Return to Chapter 3"

    else:
        print("Wrong action.")
        return "Return to Chapter 3"
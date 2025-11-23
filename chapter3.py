# chapter3_modules.py
# This file handles the exploration part of the ruins.
import time


def explore_ruins(knowledge):
    """This lets the player explore or rest to gain knowledge."""
    print("\n--- Chapter 3: The Stone Ruins ---")

    while True:
        print(f"\nKnowledge Gained: {', '.join(knowledge) if knowledge else 'None'}")

        # Player decision loop
        action = input(
            "Enter 'e' to Explore (learn secret), 'r' to Rest (dream), or 'w' to Go west (next chapter): ").lower()

        if action == 'e':
            # Adds the secret to the knowledge set
            print("Found the Crown Secret.")
            knowledge.add("Crown Secret")

        elif action == 'r':
            # Adds the vision to the knowledge set
            print("Had a dream about ancestors.")
            knowledge.add("Ancestral Vision")

        elif action == 'w':
            # Checks if the player is ready to proceed
            if "Crown Secret" in knowledge:
                print("\nGot enough knowledge. Moving on.")
                return "Proceed to Chapter 4", knowledge
            else:
                # Forces them to stay if they haven't learned enough
                print("Need more knowledge first.")

        else:
            print("Wrong button.")
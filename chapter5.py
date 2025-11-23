# chapter5_modules.py
# This file holds the code for the three game endings.

def ending_a():
    """Ending A: Be the leader (Khan)."""
    print("\n🥇 Ending A: The Khan")
    return "Ending A: Khan of Altyn Ordo"


def ending_b():
    """Ending B: Go back to the village (Return home)."""
    print("\n🏡 Ending B: The Builder")
    return "Ending B: Return Home"


def ending_c():
    """Ending C: Ride around freely (Travel freely)."""
    print("\n🐎 Ending C: The Nomad")
    return "Ending C: Free Warrior"


def choose_ending():
    """This function asks the player which ending they want."""
    print("\n--- Chapter 5: The Golden Dawn ---")

    print("\nWhat future will Bakai choose?")
    print("1. Be Khan")
    print("2. Go home")
    print("3. Travel freely")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        final_ending = ending_a()  # Calls function for Ending A
    elif choice == '2':
        final_ending = ending_b()  # Calls function for Ending B
    elif choice == '3':
        final_ending = ending_c()  # Calls function for Ending C
    else:
        print("Pick a number.")
        return choose_ending()  # Ask again if they type wrong

    print("\n*** END OF GAME ***")
    return final_ending
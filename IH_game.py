# inclusivity_adventure_game.py

import random

# Game Settings
ITEMS = ["Key", "Map", "Compass", "Sword", "Shield", "Potion", "Coin"]
TOTAL_ITEMS = 3

# IH#1: Explain (to Users) the Benefits of Using New and Existing Features
def explain_features():
    """Explain game features to the user."""
    print("\n*** Inclusivity Adventure Game ***")
    print("Welcome to the game! Your goal is to collect 3 specific items to complete the quest.")
    print("You can use commands like 'explore', 'inventory', 'undo', and 'quit' to navigate the game.")
    print("Collect the items quickly, as you are being timed!")

# IH#2: Explain Challenges
def explain_challenges():
    """Explain challenges the user may face in the game."""
    print("\nChallenges:")
    print("1. Finding specific items might take time due to randomness.")
    print("2. Exploring repeatedly can lead to duplication of items, so plan your strategy carefully.")

# IH#3: Let Users Gather as Much Information as They Want, and No More Than They Want
def provide_information():
    """Provide basic and detailed information on request."""
    info = input("\nDo you want more detailed instructions (yes/no)? ").lower()
    if info == "yes":
        print("\n** Detailed Instructions **")
        print("1. Use 'explore' to find new items.")
        print("2. Use 'inventory' to view collected items.")
        print("3. Use 'undo' to revert your last action.")
        print("4. Use 'quit' to end the game.")

# IH#4: Keep Familiar Features Available
def main_menu():
    """Main menu with consistent command options."""
    return input("\nEnter a command (explore, inventory, undo, quit): ").lower()

# IH#5: Make Undo/Redo and Backtracking Available
class GameState:
    """Class to manage game state."""
    def __init__(self):
        self.collected_items = []
        self.previous_states = []

    def save_state(self):
        """Save the current game state."""
        self.previous_states.append(self.collected_items.copy())

    def undo(self):
        """Undo the last action."""
        if self.previous_states:
            self.collected_items = self.previous_states.pop()
            print("\nReverted to previous state.")
        else:
            print("\nNo previous states to revert to.")

# IH#6: Provide an Explicit Path through the Task
def explore_area(game_state):
    """Explore and find new items."""
    game_state.save_state()
    item_found = random.choice(ITEMS)
    game_state.collected_items.append(item_found)
    print(f"\nYou found a {item_found}!")
    print(f"Items collected: {len(game_state.collected_items)} / {TOTAL_ITEMS}")

# IH#7: Provide Ways to Try Out Different Approaches
def try_different_approaches(game_state):
    """Allow users to explore alternative commands and paths."""
    command = main_menu()

    if command == "explore":
        explore_area(game_state)
    elif command == "inventory":
        print("\nInventory:", game_state.collected_items)
    elif command == "undo":
        game_state.undo()
    elif command == "quit":
        print("\nThanks for playing!")
        return False
    else:
        print("\nInvalid command, please try again.")

    return True

# IH#8: Encourage Tinkerers to Tinker Mindfully
def play_game():
    """Main game loop."""
    explain_features()
    explain_challenges()
    provide_information()

    game_state = GameState()
    keep_playing = True

    while keep_playing and len(game_state.collected_items) < TOTAL_ITEMS:
        keep_playing = try_different_approaches(game_state)

    if len(game_state.collected_items) >= TOTAL_ITEMS:
        print("\nCongratulations! You have completed the quest.")
        print(f"Collected Items: {game_state.collected_items}")

if __name__ == "__main__":
    play_game()

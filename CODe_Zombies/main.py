## Entry Point

from __future__ import annotations
from app.io_utils import *
from app.ui import *
from app.logic import *
from app.combat import *
import sys




def start() -> None:
    ensure_dirs()
    characters = load_json(DATA_DIR / "characters.json")
    weapons = load_json(DATA_DIR / "weapons.json")

    while True:
        choice = main_menu()
        if choice == "q":
            print(f"\nGoodbye.")
            sys.exit()
        elif choice == "c":
            state = load_game()
            if not state:
                print("No save found or save was corrupt.")
            else:
                print(f"Loaded: {state['player']['name']} ({state['player']['character']}) — Current Round: {state['player']['round']}")
            press_any_key()
            break
        elif choice == "n":
            # Basic name input (you can improve later)
            name = input("Enter your save name: ").strip() or "Player"
            char_id = character_select(characters)
            state = start_new_game(name, char_id, characters, weapons)
            confirm(f"\nYou chose {state['player']['character']} (favored: {state['player']['favored_type']}).")
            print("Starter weapon:", state['player']['weapon']['name'])
            print("Autosaved to saves/save.json")
            press_any_key()
            break
        else:
            print("Choose N, C, or Q.")

def run() -> None:
    ensure_dirs()
    
    state = load_game()
    while True:
        if state['player']['base_hp'] == 0:
            start()
        elif state['player']['round'] % 5 == 0:
            player_choice = between_round_menu(state)
            if player_choice == True:
                save_game(state)
            else:    
                break
        
        if state['player']['round'] % 6 == 0:
            start_combat(state, 'special')
        else:
            start_combat(state, 'standard')
        
        print_health_bar(state)

    

if __name__ == "__main__":
    
    start()
    run()

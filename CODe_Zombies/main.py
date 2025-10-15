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
            typewriter_print(f"\nGoodbye, thanks for playing!\n")
            sys.exit()
        elif choice == "c":
            state = load_game()
            if not state:
                print(f"{red}No save found or save was corrupt.{white}")
            else:
                print(f"{green}Loaded:{white} {state['player']['name']} ({state['player']['character']}) — Current Round: {red}{state['player']['round']}{white}")
            press_any_key()
            break
        elif choice == "n":
            # Basic name input (you can improve later)
            name = typewriter_input("\nEnter your save name: ").strip() or "Player"
            char_id = character_select(characters)
            state = start_new_game(name, char_id, characters, weapons)
            confirm(f"\nYou chose {state['player']['character']} (favored: {state['player']['favored_type']}).")
            typewriter_print(f"Starter weapon: {state['player']['weapon']['name']}")
            typewriter_print(f"{green}Autosaved to saves/{yellow}save.json{white}")
            press_any_key()
            break
        else:
            print("Choose N, C, or Q.")

def run() -> None:
    ensure_dirs()
    
    state = load_game()
    
    while True:
        
        
        if state['player']['base_hp'] == 0:
            state['player']['base_hp'] = 150
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
        
        


if __name__ == "__main__":
    
    start()
    run()

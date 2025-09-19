## Entry Point

from __future__ import annotations
from .io_utils import ensure_dirs, load_json, DATA_DIR
from . import ui, rng, logic

def run() -> None:
    ensure_dirs()
    characters = load_json(DATA_DIR / "characters.json")
    weapons = load_json(DATA_DIR / "weapons.json")

    while True:
        choice = ui.main_menu()
        if choice == "q":
            print("Goodbye.")
            return
        elif choice == "c":
            state = logic.load_game()
            if not state:
                print("No save found or save was corrupt.")
            else:
                print(f"Loaded: {state['player']['name']} ({state['player']['character']}) — Rounds: {state['player']['rounds_cleared']}")
            ui.press_any_key()
        elif choice == "n":
            # Basic name input (you can improve later)
            name = input("Enter your operative name: ").strip() or "Player"
            char_id = ui.character_select(characters)
            state = logic.start_new_game(name, char_id, characters, weapons)
            ui.confirm(f"\nYou chose {state['player']['character']} (favored: {state['player']['favored_type']}).")
            print("Starter weapon:", state["player"]["weapon"]["name"])
            print("Autosaved to saves/save.json")
            ui.press_any_key()
        else:
            print("Choose N, C, or Q.")

if __name__ == "__main__":
    run()

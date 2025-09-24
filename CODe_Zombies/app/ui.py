## Menus, Prompts, and Printing

from __future__ import annotations
import math

def main_menu() -> str:
    print("\n=== CODe Zombies ===")
    print("[N]ew Game   [C]ontinue  [Q]uit")
    return input("> ").strip().lower()[:1]

def between_round_menu(state) -> str:
    print("\n= Intermission =")
    print("Save & [C]ontinue   Save & [Q]uit")
    player_input = input("> ").upper()
    if player_input == 'C':
        return True
    elif player_input == 'Q':
        return False
    else:
        print("Invalid input, try again.\n>  ")
        return between_round_menu(state)
 
def print_health_bar(state):
    health_bar = "[=======================================]"

    health_step_total = health_bar.count('=')

    players_max_health = 150
    players_current_health = state['player']['base_hp']

    current_health_steps = math.floor((players_current_health / players_max_health) * health_step_total)

    health_step_string = ''

    for x in range(current_health_steps):
        health_step_string += "="

    remainder = health_step_total - current_health_steps

    for x in range(remainder):
        health_step_string += "-"

    print(f"\nPlayers Current Health:\n[{health_step_string}]")

def character_select(characters: dict) -> str:
    print("\nChoose your character:")
    keys = list(characters.keys())
    for i, k in enumerate(keys):
        print(f"    {i + 1}) {characters[k]['name']}. (favored: {characters[k]['favored_weapon']})")
    while True:
        choice = input("> ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(keys):
                return keys[idx]
        print("Invalid choice. Try again.")

def confirm(msg: str) -> None:
    print(msg)

def press_any_key() -> None:
    input("\n(press Enter to continue)\n")

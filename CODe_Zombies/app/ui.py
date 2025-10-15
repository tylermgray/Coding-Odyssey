## Menus, Prompts, and Printing

from __future__ import annotations
import math
import sys
import time
import os
from colorama import init, Fore, Back, Style


init()



red = Fore.LIGHTRED_EX
white = Fore.LIGHTWHITE_EX
blue = Fore.LIGHTBLUE_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
black = Fore.LIGHTBLACK_EX

def clear_console():
    """
    Clears the console screen based on the operating system.
    """
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

def typewriter_print(text, delay = 0.02):
    """
    Print text with a typewriter effect.

    """


    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    print() 

def typewriter_input(prompt_text):
    delay = 0.02
    for char in prompt_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    user_input = input(red + "")
    print(f"{white}")
    return user_input

def main_menu() -> str:
    typewriter_print("\n=== " + red + "COD" + white + "e " + red + "Zombies" + white + " ===\n")
    typewriter_print(f"A terminal text based game inspired by {red}Call of Duty Zombies{white}.\n")
    print(red + "[N]" + white + "ew Game" + red + "   [C]" + white + "ontinue" + red + "  [Q]" + white + "uit")
    return typewriter_input("> ").strip().lower()[:1]

def between_round_menu(state) -> str:
    typewriter_print("\n= Intermission =")
    typewriter_print("Save & [C]ontinue   Save & [Q]uit")
    player_input = input("> ").upper()
    if player_input == 'C':
        return True
    elif player_input == 'Q':
        return False
    else:
        print("Invalid input, try again.\n>  ")
        return between_round_menu(state)
 
def build_health_bar(state) -> str:
    health_bar = "[=======================================]"


    health_step_total = health_bar.count('=')

    players_max_health = 150
    players_current_health = state['player']['base_hp']

    current_health_steps = math.floor((players_current_health / players_max_health) * health_step_total)

    health_step_string = ''

    for x in range(current_health_steps):
        health_step_string += f"{green}="

    remainder = health_step_total - current_health_steps

    for x in range(remainder):
        health_step_string += f"{yellow}-"
    
   # typewriter_print(f"\nPlayers Current Health:\n")
   # print(f"[{health_step_string}{white}]")
   # typewriter_print("                  \n                  ")
    
    return f"[{health_step_string}{white}]"

def character_select(characters: dict) -> str:
    print("\nChoose your character:")
    keys = list(characters.keys())
    colors = [blue, yellow, red, green]
    for i, k in enumerate(keys):

        typewriter_print(colors[i] + f"    {i + 1}) {characters[k]['name']}. (favored: {characters[k]['favored_weapon']})" + Fore.WHITE)
    while True:
        choice = typewriter_input("> ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(keys):
                return keys[idx]
        print("Invalid choice. Try again.")
    
def confirm(msg: str) -> None:
    typewriter_print(msg)

def press_any_key() -> None:
    typewriter_input(f"\n(press {red}Enter{white} to continue)\n")

def render_text(state, text):
    time.sleep(2.00)
    points = f"      Points: {state['player']['points']}  |"
    rounds = f"Round: {state['player']['round']}  |"
    health = f"  Health: {build_health_bar(state)}"
    weapon = f"Weapon: {state['player']['weapon']['name']}"
    
    divider = "___________________"
    for x in range(health.count("[") + len(points) + len(rounds) + len(weapon)):    
        divider += "_"

    
    hud = "  ".join([health, points, rounds ,weapon])

    
    clear_console()
    print(hud)
    print(divider)
    if len(text) < 100:
        typewriter_print(text)
    else:
        typewriter_print(text, 0.003)


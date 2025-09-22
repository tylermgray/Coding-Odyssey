## Menus, Prompts, and Printing

from __future__ import annotations

def main_menu() -> str:
    print("\n=== CODe Zombies ===")
    print("[N]ew Game   [C]ontinue  [Q]uit")
    return input("> ").strip.lower()[:1]

def character_select(characters: dict) -> str:
    print("\nChoose your character:")
    keys = list(characters.keys())
    for i, k in enumerate(keys, 1):
        print(f"    {i}) {characters[k]['name']}. (favored: {characters[k]['favored_weapon']})")
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
    input("\n(press Enter to continue)")

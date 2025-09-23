from app.rng import *
from app.io_utils import *
from app.ui import *
from app.logic import *


def player_attack(state, enemy):
    player = state['player']
    player_weapon = player['weapon']
    damage_multiplier = random.randint(0, player_weapon['fire_rate'])
    damage = player_weapon['attack'] * damage_multiplier

    if damage == 0:
        print(f"\nYou need to hit the firing range, you missed...")
    else:
        print(f"\nYou did {damage} damage to {enemy['name']}!")
        enemy['base_hp'] -= damage

        if enemy['base_hp'] <= 0:
            print(f"\nYou have defeated {enemy['name']}!")
        else:
            print(f"\n{enemy['name']} has {enemy['base_hp']} health remaining.")



def player_heals(state):
        player = state['player']
        player['base_hp'] += 50
        print(f"You healed, your health is now {player['base_hp']}.")


def player_input(state):
    player = state['player']
    player_choices = ["[S]hoot", "[H]eal"]

    if player['base_hp'] == 150:
        player_choices.remove("[H]eal")
    
    player_choice = input(f"\nChoose an option:\n{"    ".join(player_choices)}\n>  ").upper()
    return player_choice


def enemy_attack(state, enemy):
    player = state['player']
    damage = enemy['attack']
    hit = random.randint(0, 1)

    if hit == 1:
        print(f"\n{enemy['name']} hit you for {damage} damage!")
        player['base_hp'] -= damage
    else:
        print(f"\n{enemy['name']} missed!")


    if player['base_hp'] <= 0:
        print(f"\nBeep bop bope beep. You died!")
    else:
        print(f"\nYou have {player['base_hp']} health remaining.")




def start_combat(state, enemy_type) -> None:
    enemies_json = load_json(DATA_DIR / "enemies.json")
    enemies = enemies_json[enemy_type]
    keys = list(enemies.keys())
    enemy = enemies[random.choice(keys)]

    print(f"\nYou've encountered a {enemy['name']}!")

    while enemy['base_hp'] > 0 and state['player']['base_hp'] > 0:
        player_choice = player_input(state)

        if player_choice == 'S':
            player_attack(state, enemy)

        elif player_choice == 'H':
             player_heals(state)

        else:
            print("Invalid input, try again.")
            return    
            
        enemy_attack(state, enemy)

    if state['player']['base_hp'] > 0:
        state['player']['round'] += 1
        print(f"\nWelcome to Round {state['player']['round']}")

        

        return True
    else:
        state['player']['round'] = 0
        return False


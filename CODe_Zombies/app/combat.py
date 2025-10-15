from app.rng import *
from app.io_utils import *
from app.ui import *
from app.logic import *



def player_attack(state, enemy):
    player = state['player']
    player_weapon = player['weapon']
    damage_bonus = player_weapon['attack_bonus']


    if random.randint(1, 5) >= 2:
        player_hit = 1
    else:
        player_hit = 0
    
    if player['favored_type'] == player_weapon['type']:
        damage_bonus += 25

    damage = (player_weapon['attack'] + damage_bonus) * player_weapon['fire_rate'] * player_hit

    gun_image = f"""⠀
 ⣤⣄⣴⣶⣿⣿⣶⣶⣦⣤⣤⣤⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣶⣀⣶⣆⣶⣦
⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿ {yellow}*{red} PEW PEW {yellow}*{white}
⢀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇ 
⠈⠛⠛⢿⣿⣿⣿⣿⣿⠛{black}⡟{white}⠛⢿⡿⠛⠛⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣿⣿⣿⣿⣿⣧⣀⣀⣀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼{black}⣿⣿⣿⣿⣿{white}⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰{black}⣿⣿⣿⣿⣿{white}⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿{black}⣿⣿⣿⣿{white}⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼{black}⣿⣿⣿⣿⣿{white}⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠉⠙⠛⠿⠿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

    render_text(state, gun_image)
    
    if damage == 0:
        render_text(state, f"\n{red}You need to hit the firing range, {yellow}you missed...{white}")
    else:
        state['player']['points'] += 10
        render_text(state, f"\nYou did {red}{damage} damage{white} to {enemy['name']}!")
        enemy['base_hp'] -= damage
        

        if enemy['base_hp'] <= 0:
            state['player']['points'] += 250
            render_text(state, f"\n{yellow}You have {red}defeated{yellow} {enemy['name']}!{white}")
            
        
        else:
            render_text(state, f"\n{enemy['name']} has {yellow}{enemy['base_hp']} health{white} remaining.")
    
    

def player_heals(state):
        player = state['player']
        player['base_hp'] += 50
        render_text(state, f"{green}You healed{white}, your health is now {green}{player['base_hp']}{white}.")


def player_input(state):
    player = state['player']
    player_choices = [f"{red}[S]{white}hoot", f"{green}[H]{white}eal"]

    if player['base_hp'] >= 150:
        player_choices.remove(f"{green}[H]{white}eal")
    
    
    player_choice = typewriter_input(f"\nChoose an option:\n{"    ".join(player_choices)}\n>  ").upper()
    if player['base_hp'] >= 150 and player_choice == 'H':
        render_text(state, "\nInvalid input. Try again\n")
        return
    return player_choice


def enemy_attack(state, enemy):
    player = state['player']
    damage = enemy['attack']
    

    hit = random.randint(0, 1)
    
    if enemy['base_hp'] > 0:
        if hit == 1:
            render_text(state, f"\n{enemy['name']} hit you for {red}{damage} damage{white}!")
            player['base_hp'] -= damage
        else:
            render_text(state, f"\n{enemy['name']} swung at you and {yellow}missed!{white}")

        if player['base_hp'] <= 0:
            typewriter_print(f"\nBeep bop bope beep. You died!")
        
    




def start_combat(state, enemy_type) -> None:
    enemies_json = load_json(DATA_DIR / "enemies.json")
    enemies = enemies_json[enemy_type]
    keys = list(enemies.keys())
    enemy = enemies[random.choice(keys)]

    
    
    if enemy['tags'] == ['normal']:
        zombie_image = f"""{black}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⢠⣾⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣼⣿⣿{yellow}⠛{black}⣿{yellow}⠛{black}⣿⣿⣿⣷⣶⣾⣿⣷⣶⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠘⠿⢻⣿⣿⡄
⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀{red}⠸{black}⠋⢿⣇
⠀⢀⣾⣿⣿⢿⣿⣿⠟⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀{red}⠁{black}
⣶⣿⣿⢿⣯⣼⡿⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠘⠻⠟⠀⠉{red}⡿{black}⠁⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀{red}⠁{black}⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡟⠀⠸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⡇⠀⠀⢿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⠋⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⣿⣿⣿⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⢿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⢘⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{white}⠀"""

        render_text(state, zombie_image)

    render_text(state, f"\nYou've encountered a {enemy['name']}!")

    while enemy['base_hp'] > 0 and state['player']['base_hp'] > 0:
        player_choice = player_input(state)

        if player_choice == 'S':
            player_attack(state, enemy)
        elif player_choice == 'H':
             player_heals(state)

        else:
            render_text(state, "Invalid input, try again.")
            return    
            
        enemy_attack(state, enemy)

    if state['player']['base_hp'] > 0:
        state['player']['round'] += 1
        typewriter_print(f"\nWelcome to {red}Round {state['player']['round']}{white}")
        

        return True
    else:
        state['player']['round'] = 0
        return False


import sys

from adventurelib import set_context

from app.Constants import game_over, instant_kill, congrats, list_of_rewards
from app.enums import Effects

greg_name = 'Greg'
pionteks_name = 'The Piontek Siblings'
tilly_name = 'Tilly'
noah_name = 'Noah'
gabe_name = 'Gabe'
cookies_name = 'Store-Bought Chocolate Chip Cookies'

character_mom = None
inventory = []
character_enemy = None
dict_enemies = {}
dict_effects = {}
dict_attacks = {}
enemy_order = [greg_name, pionteks_name, tilly_name, noah_name, gabe_name, cookies_name]
current_character_enemy_index = 0
score = 0

num_turns_in_battle = 0
battle_over = False

def end_battle(losing_character):
    '''
    This function is called when a fight ends. It handles the cases where the enemy lost, and where Mom lost
    '''
    global num_turns_in_battle
    global character_enemy
    global current_character_enemy_index
    global battle_over
    if losing_character is character_mom:
        print(game_over)
        sys.exit()

    # First, print out character defeat info
    if losing_character is dict_enemies[tilly_name] and num_turns_in_battle == 10:
        print('Because Tilly escaped defeat, Linda did not gain any points')
    else:
        global score
        score += 10
        # TODO: Increment Mom's points here and print notification of current points held

    if character_enemy == dict_enemies[cookies_name]:
        print_end_game_text()
        sys.exit()

    # Set the next enemy Mom will face, and reset her damage boost and active effect. Set context to 'break' to enable
    # break actions
    num_turns_in_battle = 0
    current_character_enemy_index += 1
    character_enemy = dict_enemies[enemy_order[current_character_enemy_index]]
    set_context('break')
    character_mom.damage_boost = 1.0
    character_mom.active_effect = Effects.NONE
    battle_over = True

def print_end_game_text():
    print(instant_kill)
    print(congrats)
    print('You have defeated all bosses! Your total score is', score, end='!')
    print(list_of_rewards)
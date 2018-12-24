import copy
import random
import sys
from adventurelib import *

from app.Constants import *
from app.enums import Effects, Attacks, Targets
from classes.attack import Attack
from classes.effect import Effect
from commands import actions

greg_name = 'Greg'
pionteks_name = 'The Piontek Siblings'
tilly_name = 'Tilly'
noah_name = 'Noah'
gabe_name = 'Gabe'
cookies_name = 'Store-Bought Chocolate Chip Cookies'

character_mom = None
mom_attacks = {}
inventory = []
character_enemy = None
dict_enemies = {}
dict_effects = {}
dict_attacks = {}
enemy_order = [greg_name, pionteks_name, tilly_name, noah_name, gabe_name, cookies_name]
current_character_enemy_index = 0

num_turns_in_battle = 0
battle_over = False


def prompt():
    if 'attacking' in get_context():
        prompt_string = f"\nLinda's health:\t{character_mom.health_remaining} / {character_mom.max_health}" \
            f"\n{character_enemy.name}'s health:\t{character_enemy.health_remaining} / {character_enemy.max_health}" \
            f"\n > "
    else:
        prompt_string = '\nLinda went to the hooga zone\n > '
    return prompt_string


def init_game_data():
    '''
    TODO: This function will load hardcoded game data from JSON file(s) as well as initializing various data structures

    We will initialize the character_mom global with Mom's character object here, as well as the dict of enemy character
    objects.

    We will also initialize the dict of attacks within attacks.py by calling the 'load_attack_data' function
    '''
    init_effect_data()
    init_attack_data()
    init_character_data()
    return

def init_attack_data():
    # TODO: This will instantiate attack objects for each individual attack and put them in the attacks dict, indexed by
    # attack name
    dict_attacks[Attacks.USE_REASON] = Attack('use reason', 15, Targets.ENEMY, Effects.NONE)
    dict_attacks[Attacks.]

    return



def init_character_data():


def init_effect_data():
    dict_effects[Effects.NONE] = Effect(Effects.NONE, '', -1)
    dict_effects[Effects.CONFUSION] = Effect(Effects.CONFUSION, 'Linda became confused!', 3)
    dict_effects[Effects.LOW_BLOOD_SUGAR] = Effect(Effects.LOW_BLOOD_SUGAR, 'Gabe got low blood sugar!\nGsbe\'s attack increased 50%!', -1)
    dict_effects[Effects.POISON] = Effect(Effects.POISON, 'Linda was poisoned by Noah\'s farts!', 3)
    dict_effects[Effects.SKIP_NEXT_TURN] = Effect(Effects.SKIP_NEXT_TURN, 'Linda lost a turn!', -1)
    dict_effects[Effects.SUPER_RELAXED] = Effect(Effects.SUPER_RELAXED, 'Linda became super relaxed!\nLinda is now invincible!', 2)


def print_start_of_game_text():
    # TODO: Print out start of game text (banner, introduction, instructions, etc.)
    print(title_banner)
    print(intro_text)
    print(instructions)

def print_new_enemy_text():


def print_health_text():
    '''
    This should be called before each of Mom's turns
    '''
    print(f'Linda\'s health:\t{character_mom.health_remaining} / {character_mom.base_health}')
    print(f'{character_enemy.name}\'s health:\t{character_mom.health_remaining} / {character_mom.base_health}')


def enemy_turn():
    '''
    This function is called at the end of any of Mom's attack functions during a battle. It will handle all logic of
    the enemy's turn (random attack choice, timing between attack being printed and flavor text being printed)
    '''
    if character_enemy is dict_enemies['Gabe'] and num_turns_in_battle == 5:
        character_enemy.active_effect = copy.deepcopy(dict_effects[Effects.Effects.LOW_BLOOD_SUGAR])
        character_enemy.damage_boost = 1.5
        character_enemy.damage_boost_turns_remaining = 1000
        print(character_enemy.active_effect.text)
    if character_enemy is dict_enemies['Tilly'] and num_turns_in_battle == 10:
        print('Tilly ran outside. The fight is over.')
        end_battle(character_enemy)

    outer_range = len(character_enemy.attacks)
    next_attack_int = random.randint(0, outer_range)
    next_attack = character_enemy.attacks[next_attack_int]


    if character_mom.active_effect.name == Effects.SUPER_RELAXED:
        print('Linda is super relaxed from the red wine. Linda is invincible!')


    # TODO: Finish implementing (need to add functionality for other effects and picking random effect/doing damage)


def end_battle(losing_character):
    '''
    This function is called when a fight ends. It handles the cases where the enemy lost, and where Mom lost
    '''
    if losing_character is character_mom:
        print(game_over)
        sys.exit()

    # First, print out character defeat info
    if losing_character is dict_enemies['Tilly'] and num_turns_in_battle == 10:
        print('Because Tilly ran outside, Linda did not gain any points')
    else:
        print(f'{losing_character.name} was defeated!')
        # TODO: Increment Mom's points here and print notification of current points held

    # Set the next enemy Mom will face, and reset her damage boost and active effect. Set context to 'break' to enable
    # break actions
    global num_turns_in_battle
    num_turns_in_battle = 0
    global current_character_enemy_index
    current_character_enemy_index += 1
    global character_enemy
    character_enemy = dict_enemies[enemy_order[current_character_enemy_index]]
    set_context('break')
    character_mom.damage_boost = 1.0
    character_mom.active_effect = Effects.NONE
    global battle_over
    battle_over = True


def start_battle():
    global battle_over
    battle_over = False
    new_context = 'attacking.'+character_enemy.name
    set_context(new_context)
    print(f'Next combatant: {character_enemy.name}!!!!')


def main():
    init_game_data()
    set_context('attacking.greg')
    global character_enemy
    character_enemy = dict_enemies['Greg']
    print_start_of_game_text()
    start()


if __name__ == '__main__':
    main()
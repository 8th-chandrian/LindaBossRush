import sys
from adventurelib import *

from app.Constants import *
from app.enums import Effects
from classes.effect import Effect
from commands import attacks

global character_mom
global mom_attacks
global items
global character_enemy
global dict_enemies
global dict_effects
global dict_attacks

global num_turns_in_battle


def init_game_data():
    '''
    TODO: This function will load hardcoded game data from JSON file(s) as well as initializing various data structures

    We will initialize the character_mom global with Mom's character object here, as well as the dict of enemy character
    objects.

    We will also initialize the dict of attacks within attacks.py by calling the 'load_attack_data' function
    '''
    items = []
    dict_enemies = {}
    dict_effects = {}
    dict_attacks = {}
    mom_attacks = {}

    init_effect_data()
    init_attack_data()
    init_character_data()
    return

def init_attack_data():
    # TODO: This will instantiate attack objects for each individual attack and put them in the attacks dict, indexed by
    # attack name
    dict_attcks[Attacks.USE_REASON] = Attack('use reason', 15, Targets.ENEMY, Effects.NONE)
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

def main():
    init_game_data()
    set_context('attacking.greg')
    character_enemy = dict_enemies['Greg']
    print_start_of_game_text()
    start()


def enemy_turn():
    '''
    This function will be called at the end of any of Mom's attack functions during a battle. It will handle all logic of
    the enemy's turn (random attack choice, timing between attack being printed and flavor text being printed)

    Ex: if Gabe fight goes on for more than x turns, he develops low blood sugar. Custom function is called every turn which
    checks if num_turns > low_blood_sugar_turns
    '''
    if character_enemy.active_effect.name is Effects.SKIP_NEXT_TURN:
        print(f'{character_enemy.name}\'s turn was skipped!')
        character_enemy.active_effect = Effects.NONE
        return
    if character_enemy is dict_enemies['Gabe'] and num_turns_in_battle == 5:
        character_enemy.damage_boost = 1.5
    if character_enemy is dict_enemies['Tilly'] and num_turns_in_battle == 10:
        print('Tilly ran outside. The fight is over.')
        end_battle(character_enemy)


def end_battle(losing_character):
    '''
    This function is called when a fight ends. It handles the cases where the enemy lost, and where Mom lost
    '''
    if losing_character is character_mom:
        print("You were defeated! Oh no...")
        # TODO: switch 'Game Over' to ASCII art text
        print(game_over)
        sys.exit()






if __name__ == '__main__':
    main()
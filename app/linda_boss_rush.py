from adventurelib import *

from commands import attacks

global character_mom
global mom_attacks
global items
global character_enemy
global dict_enemies
global dict_effects

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
    mom_attacks = {}

    init_effect_data()
    attacks.init_attack_data()
    init_character_data()
    return


def init_character_data():


def init_effect_data():



def main():
    init_game_data()
    set_context('attacking.greg')
    # TODO: Print out start of game text (banner, introduction, instructions, etc.)
    start()


def enemy_turn():
    '''
    This function will be called at the end of any of Mom's attack functions during a battle. It will handle all logic of
    the enemy's turn (random attack choice, timing between attack being printed and flavor text being printed).
    We can optionally pass in a function for custom enemy functionality which will be called on every turn.

    Ex: if Gabe fight goes on for more than x turns, he develops low blood sugar. Custom function is called every turn which
    checks if num_turns > low_blood_sugar_turns
    '''



if __name__ == '__main__':
    main()
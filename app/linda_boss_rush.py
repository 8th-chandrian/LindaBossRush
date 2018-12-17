import adventurelib

from commands import attacks

global character_mom
global character_enemy
global dict_enemies

global num_turns_in_battle


def init_game_data():
    '''
    TODO: This function will load hardcoded game data from JSON file(s) as well as initializing various data structures

    We will initialize the character_mom global with Mom's character object here, as well as the dict of enemy character
    objects.

    We will also initialize the dict of attacks within attacks.py by calling the 'load_attack_data' function
    '''
    attacks.load_attack_data()
    return


def main():
    init_game_data()
    adventurelib.start()


def enemy_turn(custom_function):
    '''
    This function will be called at the end of any of Mom's attack functions during a battle. It will handle all logic of
    the enemy's turn (random attack choice, timing between attack being printed and flavor text being printed).
    We can optionally pass in a function for custom enemy functionality which will be called on every turn.

    Ex: if Gabe fight goes on for more than x turns, he develops low blood sugar. Custom function is called every turn which
    checks if num_turns > low_blood_sugar_turns
    '''


if __name__ == '__main__':
    main()
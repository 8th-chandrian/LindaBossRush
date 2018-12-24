import sys
from adventurelib import *

from app.enums import Effects
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

global num_turns_in_battle


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


def init_character_data():


def init_effect_data():
    dict_effects[Effects.NONE] = Effect(Effects.NONE, '', -1)
    dict_effects[Effects.CONFUSION] = Effect(Effects.CONFUSION, 'Linda became confused!', 3)
    dict_effects[Effects.LOW_BLOOD_SUGAR] = Effect(Effects.LOW_BLOOD_SUGAR, 'Gabe got low blood sugar!\nGsbe\'s attack increased 50%!', -1)
    dict_effects[Effects.POISON] = Effect(Effects.POISON, 'Linda was poisoned by Noah\'s farts!', 3)
    dict_effects[Effects.SKIP_NEXT_TURN] = Effect(Effects.SKIP_NEXT_TURN, 'Linda lost a turn!', -1)
    dict_effects[Effects.SUPER_RELAXED] = Effect(Effects.SUPER_RELAXED, 'Linda became super relaxed!\nLinda is now invincible!', 2)

def init_attack_data():

    return

def print_start_of_game_text():
    # TODO: Print out start of game text (banner, introduction, instructions, etc.)

def print_new_enemy_text():
    

def main():
    init_game_data()
    set_context('attacking.greg')
    global character_enemy
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
        print("GAME OVER")
        sys.exit()

    # First, print out character defeat info
    print(f'{losing_character.name} was defeated!')
    # TODO: Increase Mom's points here and print notification

    # Set the next enemy Mom will face, and reset her damage boost and active effect. Set context to 'break' to enable
    # break actions
    global current_character_enemy_index
    current_character_enemy_index += 1
    global character_enemy
    character_enemy = dict_enemies[enemy_order[current_character_enemy_index]]
    set_context('break')
    character_mom.damage_boost = 1.0
    character_mom.active_effect = Effects.NONE

def start_battle():
    new_context = 'attacking.'+character_enemy.name
    set_context(new_context)
    print(f'Next combatant: {character_enemy.name}!!!!')




if __name__ == '__main__':
    main()
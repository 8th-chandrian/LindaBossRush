#########################################
#           Enemy Attacks               #
#########################################
# TODO: change "character used attack" to "character attacked", also add punctuation
##### Greg's Attacks #####
from app.enums import Attacks
from app.globals import *


def mild_sexism():
    attack_data = dict_attacks[Attacks.MILD_SEXISM]
    damage = attack_data.damage * character_enemy.damage_boost
    print('Greg used "mild sexism"')
    print('Greg said something mildly sexist! (Come on, dude...)')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)

def sell_company():
    attack_data = dict_attacks[Attacks.SELL_COMPANY]
    damage = attack_data.damage * character_enemy.damage_boost
    print('Greg used "sell company"')
    print('Greg sold Brand Integrity for fat stacks of cash! Linda now works for Reward Gateway...what a cruddy name')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)

def ignore_advice():
    attack_data = dict_attacks[Attacks.IGNORE_ADVICE]
    damage = attack_data.damage * character_enemy.damage_boost
    print('Greg used "ignore advice"')
    print('Greg ignored the frankly quite helful advice of his underlings,\nhurting himself in the process')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    print(f'{character_enemy.name} did {damage} points of damage to Greg')
    character_mom.decrement_health(damage)
    character_enemy.decrement_health(damage)

def blame_linda():
    attack_data = dict_attacks[Attacks.IGNORE_ADVICE]
    damage = attack_data.damage * character_enemy.damage_boost
    print('Greg used "blame linda"')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)


##### Piontek Siblings' Attacks #####
def vote_trump():
    attack_data = dict_attacks[Attacks.VOTE_TRUMP]
    damage = attack_data.damage * character_enemy.damage_boost
    print('The Piontek Siblings used "vote for trump"')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)

def insist_dinner_siblings():
    attack_data = dict_attacks[Attacks.INSIST_DINNER_SIBLINGS]
    damage = attack_data.damage * character_enemy.damage_boost
    print('The Piontek Siblings used "insist on paying for dinner"')
    print('Linda feels bad for not paying')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)

def pick_on_linda():
    attack_data = dict_attacks[Attacks.PICK_ON_LINDA]
    damage = attack_data.damage * character_enemy.damage_boost
    print('The Piontek Siblings used "pick on linda"')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)


##### Tilly's Attacks #####
def scarf_and_barf():
    attack_data = dict_attacks[Attacks.SCARF_AND_BARF]
    damage = attack_data.damage * character_enemy.damage_boost
    print('Tilly used "scarf and barf"')
    print('Ewww! Gaaaabe!')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)

def dead_mouse():
    attack_data = dict_attacks[Attacks.DEAD_MOUSE]
    damage = attack_data.damage * character_enemy.damage_boost
    print('Tilly used "dead mouse surprise')
    print('Linda feels bad for that poor mouse')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)

def alive_mouse():
    attack_data = dict_attacks[Attacks.ALIVE_MOUSE]
    damage = attack_data.damage * character_enemy.damage_boost
    print('Tilly used "dead mouse surprise"')
    print('Wait, is it dead?')
    print('Tilly used "alive mouse surprise"')
    print('Oh no! The mouse is still alive! Linda fled from the room!')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)

def hairball():
    attack_data = dict_attacks[Attacks.HAIRBALL]
    damage = attack_data.damage * character_enemy.damage_boost
    print('Tilly used "hairball"')
    print('Gross!')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)

##### Gabe's Attacks #####
def sleep_till_3():
    # TODO: This heals, Noah pls do this one

def gabe_out():

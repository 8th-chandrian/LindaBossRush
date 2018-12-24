#########################################
#           Enemy Attacks               #
#########################################

##### Greg's Attacks #####
from app.enums import Attacks
from app.globals import dict_attacks, character_enemy, character_mom


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
    print('Greg sold Brand Integrity! Linda now works for Reward Gateway...what a cruddy name')
    print(f'{character_enemy.name} did {damage} points of damage to Linda')
    character_mom.decrement_health(damage)
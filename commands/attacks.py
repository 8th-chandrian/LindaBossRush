from adventurelib import *

from app.enums import *
from app.linda_boss_rush import *
from classes.attack import Attack


#########################################
#           Mom's Attacks               #
#########################################

@when("use reason", context='attacking.greg')
@when("use reason", context='attacking.pionteks')
@when("use reason", context='attacking.tilly')
def use_reason():
    attack_data = dict_attacks['use reason']
    if get_context() == 'attacking.tilly':
        print('It has no effect. Tilly is a cat. Duh.')
        return
    character_enemy.decrement_health(attack_data.damage * character_mom.damage_boost)
    # TODO: finish writing method
    enemy_turn(character_enemy.custom_function)


@when("use ITEM", context='attacking')
def use_item(item):
    if item not in items:
        print(f'You do not have any {item}')
        return
    else:
        print(f'Mom used {item}')
        # TODO: include code here to have a delay (maybe .5 seconds) between these two lines being printed
        if item.lower() == 'dark chocolate':
            # TODO: Print item effect data
            character_mom.health += 50
        elif item.lower() == 'coffee':
            # TODO: Print item effect data
            character_mom.damage_boost = 1.2
            # TODO: Finish implementing
    enemy_turn(character_enemy.custom_function)




#########################################
#           Enemy Attacks               #
#########################################
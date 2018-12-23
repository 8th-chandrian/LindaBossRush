from adventurelib import *

from app.enums import *
from app.linda_boss_rush import *
from classes.attack import Attack

attacks_data = {}

def init_attack_data():
    # TODO: This will instantiate attack objects for each individual attack and put them in the attacks dict, indexed by
    # attack name
    use_reason_attack = Attack('use reason', 15, Targets.ENEMY, Effects.NONE)
    attacks_data[use_reason_attack.name] = use_reason_attack
    return


#########################################
#           Mom's Attacks               #
#########################################

@when("use reason", context='attacking.greg')
@when("use reason", context='attacking.pionteks')
@when("use reason", context='attacking.tilly')
def use_reason():
    attack_data = attacks_data['use reason']
    if get_context() == 'attacking.tilly':
        print('It has no effect. Tilly is a cat. Duh.')
        return
    print(attack_data.text)
    character_enemy.decrement_health(20)
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
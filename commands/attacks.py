from adventurelib import *
from app.linda_boss_rush import *

attacks = {}

def load_attack_data():
    # TODO: This will instantiate attack objects for each individual attack and put them in the attacks dict, indexed by
    # attack name
    return


#########################################
#           Mom's Attacks               #
#########################################

@when("use reason", context='attacking.greg')
@when("use reason", context='attacking.pionteks')
@when("use reason", context='attacking.tilly')
def use_reason():
    attack_data = attacks['use_reason']
    if get_context() == 'attacking.tilly':
        print('It has no effect. Tilly is a cat. Duh.')
        return
    print(attack_data.text)
    character_enemy.decrement_health(20)
    # TODO: finish writing method
    enemy_turn(character_enemy.custom_function)


@when("use ITEM", context='attacking')
def use_item(item):
    item_data = character_mom.items[item]
    if not item_data:
        print(f'You do not have any {item}')
    else:
        print(f'Mom used {item}')
        # TODO: include code here to have a delay (maybe .5 seconds) between these two lines being printed
        print(item_data.text)
        if item_data.name.lower() == 'dark chocolate':
            character_mom.health += 50
        elif item_data.name.lower() == 'coffee':
            character_mom.damage_boost = 1.2
            # TODO: Finish implementing
    enemy_turn(character_enemy.custom_function)




#########################################
#           Enemy Attacks               #
#########################################
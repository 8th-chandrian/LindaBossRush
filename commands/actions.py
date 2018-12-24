import copy

from adventurelib import *

from app.enums import *
from app.linda_boss_rush import *
from classes.attack import Attack


#########################################
#         Mom's Break Actions           #
#########################################

@when("brew coffee", context='break')
def brew_coffee():
    print('Linda brewed a cup of coffee.')
    print('One cup of coffee has been added to your inventory!')
    inventory.append('coffee')
    start_battle()


@when("go to Wegmans", context='break')
def go_to_wegmans():
    print('Linda went to Wegmans and bought dark chocolates.')
    print('Two dark chocolates have been added to your inventory!')
    inventory.append('dark chocolate')
    inventory.append('dark chocolate')
    start_battle()


@when("drink red wine", context='break')
def drink_red_wine():
    print('Linda drank a glass of red wine.')
    character_mom.active_effect = copy.deepcopy(dict_effects[Effects.SUPER_RELAXED])
    print(character_mom.active_effect.text)
    start_battle()


@when("eat out at Jojo", context='break')
def eat_out():
    print('Linda went out and got dinner at Jojo')
    print('It was a really good dinner. Linda\'s base health increased by 20 points!')
    character_mom.max_health += 20
    start_battle()


@when("go to Body Pump class", context='break')
def go_to_body_pump():
    print('Linda went to Body Pump.')
    print('Linda got PUMPED! Linda\'s attack damage increased!')
    character_mom.damage_boost = 1.3
    start_battle()



#########################################
#           Mom's Attacks               #
#########################################

@when("use reason", context='attacking.Greg')
@when("use reason", context='attacking.The Piontek Siblings')
@when("use reason", context='attacking.Tilly')
def use_reason():
    if character_mom.apply_active_effect():
        enemy_turn()
        return
    attack_data = dict_attacks['use reason']
    if get_context() == 'attacking.tilly':
        print('It has no effect. Tilly is a cat. Duh.')
        enemy_turn()
        return
    character_enemy.decrement_health(attack_data.damage * character_mom.damage_boost)
    enemy_turn()
    return


@when("use ITEM", context='attacking')
def use_item(item):
    if character_mom.apply_active_effect():
        enemy_turn()
        return
    if item not in inventory:
        print(f'You do not have any {item}')
        return
    else:
        inventory.remove(item)
        print(f'Linda used {item}')
        if item.lower() == 'dark chocolate':
            print('Linda was healed for 20 points!')
            character_mom.heal(20)
        elif item.lower() == 'coffee':
            print('Linda got wired! Linda\'s attack damage increased!')
            character_mom.damage_boost += 0.2
        else:
            print("ERROR: SOMETHING GOT MESSED UP!!!!!")
    enemy_turn()
    return


@when("view inventory")
def view_inventory():
    print("Your inventory contains:")
    for item in inventory:
        print(f'\t{item}')
    return



#########################################
#           Enemy Attacks               #
#########################################
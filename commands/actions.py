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
        if battle_over:
            return
        else:
            enemy_turn()
            return
    if battle_over:
        return

    attack_data = dict_attacks[Attacks.USE_REASON]
    if get_context() == 'attacking.tilly':
        print('It has no effect. Tilly is a cat. Duh.')
        enemy_turn()
        return
    else:
        print('Linda used "use reason"')
        damage = attack_data.damage * character_mom.damage_boost
        print(f'Linda did {damage} points of damage to {character_enemy.name}')
        character_enemy.decrement_health(damage)
        if battle_over:
            return
        else:
            enemy_turn()
            return

@when("roundhouse kick", context='attacking.Greg')
def roundhouse_kick():
    if character_mom.apply_active_effect():
        if battle_over:
            return
        else:
            enemy_turn()
            return
    if battle_over:
        return

    attack_data = dict_attacks[Attacks.KICK]
    print('Linda used "roundhouse kick"')
    damage = attack_data.damage * character_mom.damage_boost
    print(smash)
    print(f'Linda did {damage} points of damage to {character_enemy.name}')
    character_enemy.decrement_health(damage)
    if battle_over:
        return
    else:
        enemy_turn()
        return


@when("close a big sale", context='attacking.Greg')
def close_sale():
    if character_mom.apply_active_effect():
        if battle_over:
            return
        else:
            enemy_turn()
            return
    if battle_over:
        return

    attack_data = dict_attacks[Attacks.BIG_SALE]
    print('Linda used "close a big sale"')
    damage = attack_data.damage * character_mom.damage_boost
    print('Yay! (fingers apart)')
    print(f'Linda did {damage} points of damage to {character_enemy.name}')
    character_enemy.decrement_health(damage)
    if battle_over:
        return
    else:
        enemy_turn()
        return

@when("bake chocolate chip cookies", context='attacking.Gabe')
@when("bake chocolate chip cookies", context='attacking.Store-Bought Chocolate Chip Cookies')
def bake_cookies():
    if character_mom.apply_active_effect():
        if battle_over:
            return
        else:
            enemy_turn()
            return
    if battle_over:
        return

    attack_data = dict_attacks[Attacks.COOKIES]
    print('Linda used "bake chocolate chip cookies"')
    if character_enemy == dict_enemies[cookies_name]:
        print(instant_kill)
        print('The store-bought cookies could not compete!')
        print_end_game_text()
        sys.exit()


@when("use ITEM", context='attacking')
def use_item(item):
    if character_mom.apply_active_effect():
        if battle_over:
            return
        else:
            enemy_turn()
            return
    if battle_over:
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
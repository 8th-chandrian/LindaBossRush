from adventurelib import set_context, start

from app.globals import dict_enemies
from app.linda_boss_rush import init_game_data, print_start_of_game_text
import commands.actions


def main():
    init_game_data()
    set_context('attacking.Greg')
    global character_enemy
    character_enemy = dict_enemies['Greg']
    print_start_of_game_text()
    start()


if __name__ == '__main__':
    main()
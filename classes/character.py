import random

from app.enums import Effects
from app.globals import dict_effects, battle_over, end_battle


class Character:

    # TODO: Finish implementing class

    def __init__(self, name, health, attacks):
        self.name = name
        self.max_health = health
        self.health_remaining = health
        self.attacks = attacks
        self.damage_boost = 1.0
        self.damage_boost_turns_remaining = 0
        self.active_effect = dict_effects[Effects.NONE]

    def decrement_health(self, health_lost):
        '''
        :param health_lost:
        '''
        print(f'{self.name} took {health_lost} points of damage')
        if health_lost >= self.health_remaining:
            print(f'{self.name} was defeated!')
            end_battle(self)
            return
        else:
            self.health_remaining -= health_lost
            return


    def increment_health(self, health_gained):
        self.health_remaining += health_gained
        if self.health_remaining > self.max_health:
            self.health_remaining = self.max_health


    def apply_active_effect(self):
        '''
        :return: True if Mom's turn is skipped, False otherwise
        '''
        if self.active_effect.name == Effects.NONE:
            return False

        # Check if effect is still active
        if self.active_effect.turns_effective == 0:
            if self.active_effect.name == Effects.SUPER_RELAXED:
                print(f'{self.name} is no longer super relaxed.')
            elif self.active_effect.name == Effects.CONFUSION:
                print(f'{self.name} is no longer confused.')
            elif self.active_effect.name == Effects.POISON:
                print(f'The fart dispersed. {self.name} is no longer taking toxic damage.')
            self.active_effect = dict_effects[Effects.NONE]
            return False

        self.active_effect.turns_effective -= 1

        # If the effect is still active, handle it
        if self.active_effect.name == Effects.SKIP_NEXT_TURN:
            print(f'{self.name} was laughing too hard to do anything.')
            return True
        elif self.active_effect.name == Effects.POISON:
            print(f'{self.name} took 10 points of toxic damage from the lingering fart!')
            self.decrement_health(10)
            if battle_over:
                return True
            return False
        elif self.active_effect.name == Effects.CONFUSION:
            print(f'{self.name} is confused!')
            if random.randint(0,10) < 5:
                print(f'{self.name} hurt herself in her confusion!')
                self.decrement_health(10)
                if battle_over:
                    return True
                return True
            else:
                return False
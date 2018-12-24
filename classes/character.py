from app.enums import Effects


class Character:

    # TODO: Finish implementing class

    def __init__(self, name, health):
        self.name = name
        self.max_health = health
        self.health_remaining = health
        self.damage_boost = 1.0
        self.damage_boost_turns_remaining = 0
        self.active_effect = Effects.NONE

    def decrement_health(self, health_lost):
        print(f'{self.name} took {health_lost} points of damage')
        if health_lost >= self.health_remaining:
            print(f'{self.name} was defeated!')
            # TODO: Handle case where enemy/Mom is defeated
        else:
            self.health_remaining -= health_lost


    def increment_health(self, health_gained):
        self.health_remaining += health_gained
        if self.health_remaining > self.max_health:
            self.health_remaining = self.max_health


    def apply_active_effect(self):

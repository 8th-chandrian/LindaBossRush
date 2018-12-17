class character:

    # TODO: Finish implementing class

    def __init__(self, name, health, custom_function):
        self.name = name
        self.max_health = health
        self.health_remaining = health
        self.custom_function = custom_function

    def decrement_health(self, health_lost):
        print(f'{self.name} took {health_lost} points of damage')
        if health_lost >= self.health_remaining:
            print(f'{self.name} was defeated!')
            # TODO: Handle case where enemy/Mom is defeated
        else:
            self.health_remaining -= health_lost
class Character:

    def __init__(self, name, health, attacks, active_effect):
        self.name = name
        self.max_health = health
        self.health_remaining = health
        self.attacks = attacks
        self.damage_boost = 1.0
        self.damage_boost_turns_remaining = 0
        self.active_effect = active_effect
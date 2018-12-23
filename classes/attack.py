class Attack:

    def __init__(self, name, damage, target, effect):
        self.name = name
        self.damage = damage
        self.target = target
        self.effect = effect
        self.is_disabled = False


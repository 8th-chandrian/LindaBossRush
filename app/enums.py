from enum import Enum


class Targets(Enum):
    SELF = 1
    ENEMY = 2
    BOTH = 3


class Effects(Enum):
    SKIP_NEXT_TURN = 1
    SUPER_RELAXED = 2
    CONFUSION = 3
    POISON = 4
    LOW_BLOOD_SUGAR = 5
    NONE = 6
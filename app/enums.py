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

class Attacks(Enum):

    # Mom's attacks
    USE_REASON = 1
    COOKIES = 2
    KICK = 3
    BACH = 4
    YAY = 5
    BIG_SALE = 7
    GIVE_ADVICE = 8
    INCORRECT_REFERENCE = 9
    GABE_COAT = 10
    LONG_TIME_MAKEUP = 11
    WATER_DOWN_COFFEE = 12
    INSIST_ON_UBER = 13
    CHANGE_SUBJECT = 14
    INSIST_DINNER_LINDA = 15
    AIR_CANNON = 16
    CALL_GABE = 17
    YELL_AT_TILLY = 18

    # Greg's Attacks
    MILD_SEXISM = 19
    SELL_COMPANY = 20
    IGNORE_ADVICE = 21
    BLAME_LINDA = 22

    # Piontek Siblings' Attacks
    VOTE_TRUMP = 23
    INSIST_DINNER_SIBLINGS = 24
    PICK_ON_LINDA = 25

    # Tilly's Attacks
    SCARF_AND_BARF = 26
    DEAD_MOUSE = 27
    ALIVE_MOUSE = 28
    HAIRBALL = 29

    # Gabe's Attacks
    SLEEP_TILL_3 = 30
    GABE_OUT = 31
    STOP = 32
    OBSCURE_REFERENCE = 33

    # Noah's Attacks
    TOXIC_FART = 34
    HANGER = 35
    SAY_FAM = 36
    HERPDY_DERP = 37

    # Store-Bought Cookie's Attacks
    LOOK_TASTY = 38
    SIT_THERE = 39

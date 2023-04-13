__version__ = "0.0.1"

KEYCAPS_DIGIT = "%d\uFE0F\u20E3"
KEYCAPS_TEN = "\u1F51F"
GAME_DIE = "🎲"

DIGITS = {n: (KEYCAPS_DIGIT % n) for n in range(10)}
DIGITS[10] = KEYCAPS_TEN


def emojize(number: int) -> str:
    """Convert any integer number into emoji digits"""

    try:
        number = abs(int(number))
    except ValueError as e:
        raise ValueError("Only integer numbers could be emojized")
    else:
        if number in range(0, 9):
            return DIGITS[number]
        return " ".join([DIGITS[int(d)] for d in str(number)])

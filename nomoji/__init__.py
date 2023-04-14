KEYCAPS_DIGITS = ["\0030\uFE0F\u20E3",
                 "\0031\uFE0F\u20E3",
                 "\0032\uFE0F\u20E3",
                 "\0033\uFE0F\u20E3",
                 "\0034\uFE0F\u20E3",
                 "\0035\uFE0F\u20E3",
                 "\0036\uFE0F\u20E3",
                 "\0037\uFE0F\u20E3",
                 "\0038\uFE0F\u20E3",
                 "\0039\uFE0F\u20E3",
                 "\u1F51F"
                 ]
GAME_DIE = "🎲"

DIGITS = {n: KEYCAPS_DIGITS[n] for n in range(11)}


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

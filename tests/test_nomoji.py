import pytest
from nomoji import DIGITS, GAME_DIE
from nomoji import emojize


def test_game_die():
    assert GAME_DIE == "🎲"


def test_all_digits():
    assert len(DIGITS) == 11, "Not all numbers in Digits"
    assert all(k in range(0, 11) for k in DIGITS)


def test_emojize_on_non_numbers_raises_exception():
    with pytest.raises(ValueError):
        emojize("non number")


def test_emojize_on_numbers_as_strings():
    assert emojize("2") == DIGITS[2]
    assert emojize("4") == DIGITS[4]
    assert emojize("24") == f"{DIGITS[2]} {DIGITS[4]}"


def test_emojize_on_float_numbers():
    assert emojize(1.3) == DIGITS[1]


def test_emojize_on_negative_ints():
    assert emojize(-9) == DIGITS[9]

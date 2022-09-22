import pytest


def always_returns_true():
<<<<<<< HEAD
    print("Wow, Jamaica is the best.")
=======
    print("Hello")
>>>>>>> ae91a77ab56e1a893af5f3b2de8c351501d27813
    return False


def test_always_returns_true():
    assert always_returns_true()

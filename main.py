import pytest


def always_returns_true():
<<<<<<< HEAD
    print("Hello Again")
    print("Bye")
=======
<<<<<<< HEAD
    print("Wow, Jamaica is the best.")
=======
    print("Hello")
>>>>>>> ae91a77ab56e1a893af5f3b2de8c351501d27813
>>>>>>> d3eec9e0cf762ac5e9ef5fcca28813ef1905470f
    return False


def test_always_returns_true():
    assert always_returns_true()

import pytest


def always_returns_true():
    print("Wow, Jamaica is the best.")
    return False


def test_always_returns_true():
    assert always_returns_true()

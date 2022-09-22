import pytest


def always_returns_true():
    print("Hello Again")
    print("Bye")
    return False


def test_always_returns_true():
    assert always_returns_true()

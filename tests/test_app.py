import pytest
from app import add, is_even

def test_add_simple():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
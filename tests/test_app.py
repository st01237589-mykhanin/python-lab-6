import pytest
from app import add, is_even

def test_add_simple():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2
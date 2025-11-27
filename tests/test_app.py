import pytest
from app import add, is_even

def test_add_simple():
    assert add(2, 3) == 5
import pytest
# test_math_functions.py
from math_functions import add, multiply

def test_add():
    assert add(2, 3) == 6, \
    'it is 6'
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0

pytest.main(["-v", "--tb=line", "-rN", __file__])
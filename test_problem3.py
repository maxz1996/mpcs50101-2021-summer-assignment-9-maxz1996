# Max Zinski
# tests for problem3

import pytest
from problem3 import max_number

def test_max_number_fn():
    assert max_number([1,2,3,4,5]) == 5
    assert max_number([1,2,5,3,4]) == 5
    assert max_number([1, 2.0, 3.5, 3]) == 3.5
    assert max_number({1, 2, 4, 5}) == None
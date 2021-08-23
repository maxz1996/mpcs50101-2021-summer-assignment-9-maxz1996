# Max Zinski
# test suite for problem4 

import pytest
from problem4 import prune_invalid_types, product_of_odds

def test_pruner():
    assert prune_invalid_types(3) == 3
    assert prune_invalid_types(3.0) == 3.0
    assert prune_invalid_types(2.5) == 1
    assert prune_invalid_types("apple") == 1

def test_product_of_odds():
    assert product_of_odds([1,3,5,7]) == 105
    assert product_of_odds([1, 2, 3, 4, 5, 7]) == 105
    assert product_of_odds([1, "3", 5, "apple"]) == 5
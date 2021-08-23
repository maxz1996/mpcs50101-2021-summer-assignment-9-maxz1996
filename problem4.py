# Max zinski
# Problem 4

from functools import reduce
from typing import List

"""
When called in the context of product_of_oddss, will prune any invalid types, so the filter expression can mod them.
Arguments that are not equal to itself when converted to an integer will be set to 1. In this way, the invalid elements will not 
interfere with the calculate of the product of odds.
"""
def prune_invalid_types(el):
    try:
        if int(el) != el:
            return 1
        else:
            return el
    # element could not be converted to an integer
    except:
        return 1

def product_of_odds(list):
    return reduce(lambda a, b: a * b, \
      filter(lambda x: x % 2, \
          map(prune_invalid_types, list)))

# sample use case
print(product_of_odds([0,3.3, "apple", 2,3,4, 5, 7, 9, 9]))
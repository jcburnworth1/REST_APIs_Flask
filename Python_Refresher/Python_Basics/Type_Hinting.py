##### Type Hinting Basics #####
from typing import List

## Basic function - No hinting which isn't very helpful
# def list_avg(sequence):
#     return sum(sequence) / len(sequence)
#
# avg = list_avg([1,2,3])

## Basic function - With hinting
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

avg = list_avg([3,4,5])
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from add import Add


def test_add_positive_numbers():
    adder = Add(5, 7)
    assert adder.compute() == 12

def test_add_negative_numbers():
    adder = Add(-3, -6)
    assert adder.compute() == -9

def test_add_mixed_numbers():
    adder = Add(-5, 10)
    assert adder.compute() == 5

def test_add_zero():
    adder = Add(0, 0)
    assert adder.compute() == 0

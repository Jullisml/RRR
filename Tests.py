import pytest

from SpecialHashMap import SpecialHashMap


def test_iloc_with_sorted_items():
    map = SpecialHashMap()
    map["value1"] = 1
    map["1"] = 10
    map["3"] = 30
    map["10, 5"] = 300
    assert map.iloc == [10, 300, 30, 1]

def test_iloc_without_items():
    map = SpecialHashMap()
    assert map.iloc == []


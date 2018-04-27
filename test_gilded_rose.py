import pytest

from gilded_rose import Item, GildedRose

@pytest.fixture
def foo_item():
    name = 'foo'
    items = [Item(name, 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return items[0]


def test_foo(foo_item):
    assert foo_item.quality == 9
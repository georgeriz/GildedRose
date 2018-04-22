import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def update_item(self, name, sell_in, quality):
        items = [Item(name, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        return items[0]
        
    def test_foo_before_sellin(self):
        item = self.update_item(name="foo", sell_in=10, quality=50)
        self.assertEquals(49, item.quality)

    def test_foo_after_sellin(self):
        item = self.update_item(name="foo", sell_in=0, quality=50)
        self.assertEquals(48, item.quality)

    def test_foo_zero_quality_after_sellin(self):
        item = self.update_item(name="foo", sell_in=0, quality=0)
        self.assertEquals(0, item.quality)

    def test_brie_increases(self):
        item = self.update_item(name = "Aged Brie", sell_in=10, quality=5)
        self.assertEquals(6, item.quality)

    def test_brie_no_more_than_fifty(self):
        item = self.update_item(name="Aged Brie", sell_in=10, quality=50)
        self.assertEquals(50, item.quality)

    def test_sulfuras_before_sellin(self):
        item = self.update_item(name="Sulfuras", sell_in=10, quality=80)
        self.assertEquals(80, item.quality)

    def test_sulfuras_after_sellin(self):
        item = self.update_item(name="Sulfuras", sell_in=0, quality=80)
        self.assertEquals(80, item.quality)  

    def test_backstage_after_ten_sellin(self):
        item = self.update_item(name="Backstage", sell_in=10, quality=5)
        self.assertEquals(7, item.quality)

    def test_backstage_no_more_than_fifty_after_ten_sellin(self):
        item = self.update_item(name="Backstage", sell_in=10, quality=50)
        self.assertEquals(50, item.quality)

    def test_backstage_after_five_sellin(self):
        item = self.update_item(name="Backstage", sell_in=5, quality=5)
        self.assertEquals(8, item.quality)

    def test_backstage_no_more_than_fifty_after_five_sellin(self):
        item = self.update_item(name="Backstage", sell_in=5, quality=50)
        self.assertEquals(50, item.quality)

    def test_backstage_after_sellin(self):
        item = self.update_item(name="Backstage", sell_in=0, quality=50)
        self.assertEquals(0, item.quality)

    def test_conjured_before_sellin(self):
        item = self.update_item(name="Conjured", sell_in=10, quality=50)
        self.assertEquals(48, item.quality)

    def test_conjured_after_sellin(self):
        item = self.update_item(name="Conjured", sell_in=0, quality=50)
        self.assertEquals(46, item.quality)

    def test_conjured_zero_quality_after_sellin(self):
        item = self.update_item(name="Conjured", sell_in=0, quality=1)
        self.assertEquals(0, item.quality)

if __name__ == '__main__':
    unittest.main()
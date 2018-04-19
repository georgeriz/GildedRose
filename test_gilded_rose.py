import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def update_item(self, name, sell_in, quality):
        items = [Item(name, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        return items[0]
        
    def test_foo_before_sellin(self):
        item = self.update_item(name="foo", sell_in=11, quality=50)
        self.assertEquals(49, item.quality)

    def test_foo_after_sellin(self):
        item = self.update_item(name="foo", sell_in=0, quality=50)
        self.assertEquals(48, item.quality)

    def test_foo_zero_quality_after_sellin(self):
        item = self.update_item(name="foo", sell_in=0, quality=0)
        self.assertEquals(0, item.quality)

    def test_Brie(self):
        name = "Aged Brie"
        sell_in = [11, 10, 6, 5, 0, -1]
        quality = [50, 49, 1, 0]
        items = [Item(name, s, q) for s in sell_in for q in quality]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
        self.assertEquals(50, items[1].quality)
        self.assertEquals(2, items[2].quality)
        self.assertEquals(1, items[3].quality)
        self.assertEquals(50, items[4].quality)
        self.assertEquals(50, items[5].quality)
        self.assertEquals(2, items[6].quality)
        self.assertEquals(1, items[7].quality)
        self.assertEquals(50, items[8].quality)
        self.assertEquals(50, items[9].quality)
        self.assertEquals(2, items[10].quality)
        self.assertEquals(1, items[11].quality)
        self.assertEquals(50, items[12].quality)
        self.assertEquals(50, items[13].quality)
        self.assertEquals(2, items[14].quality)
        self.assertEquals(1, items[15].quality)
        self.assertEquals(50, items[16].quality)
        self.assertEquals(50, items[17].quality)
        self.assertEquals(3, items[18].quality)
        self.assertEquals(2, items[19].quality)
        self.assertEquals(50, items[20].quality)
        self.assertEquals(50, items[21].quality)
        self.assertEquals(3, items[22].quality)
        self.assertEquals(2, items[23].quality)

    def test_Sulfuras(self):
        name = "Sulfuras"
        sell_in = [11, 10, 6, 5, 0, -1]
        items = [Item(name, s, 80) for s in sell_in]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for item in items:
            self.assertEquals(80, item.quality)

    def test_Backstage(self):
        name = "Backstage"
        sell_in = [11, 10, 6, 5, 0, -1]
        quality = [50, 49, 1, 0]
        items = [Item(name, s, q) for s in sell_in for q in quality]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
        self.assertEquals(50, items[1].quality)
        self.assertEquals(2, items[2].quality)
        self.assertEquals(1, items[3].quality)
        self.assertEquals(50, items[4].quality)
        self.assertEquals(50, items[5].quality)
        self.assertEquals(3, items[6].quality)
        self.assertEquals(2, items[7].quality)
        self.assertEquals(50, items[8].quality)
        self.assertEquals(50, items[9].quality)
        self.assertEquals(3, items[10].quality)
        self.assertEquals(2, items[11].quality)
        self.assertEquals(50, items[12].quality)
        self.assertEquals(50, items[13].quality)
        self.assertEquals(4, items[14].quality)
        self.assertEquals(3, items[15].quality)
        self.assertEquals(0, items[16].quality)
        self.assertEquals(0, items[17].quality)
        self.assertEquals(0, items[18].quality)
        self.assertEquals(0, items[19].quality)
        self.assertEquals(0, items[20].quality)
        self.assertEquals(0, items[21].quality)
        self.assertEquals(0, items[22].quality)
        self.assertEquals(0, items[23].quality)

    def test_Conjured(self):
        name = "Conjured"
        sell_in = [11, 10, 6, 5, 0, -1]
        quality = [50, 49, 1, 0]
        items = [Item(name, s, q) for s in sell_in for q in quality]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(48, items[0].quality)
        self.assertEquals(47, items[1].quality)
        self.assertEquals(0, items[2].quality)
        self.assertEquals(0, items[3].quality)
        self.assertEquals(48, items[4].quality)
        self.assertEquals(47, items[5].quality)
        self.assertEquals(0, items[6].quality)
        self.assertEquals(0, items[7].quality)
        self.assertEquals(48, items[8].quality)
        self.assertEquals(47, items[9].quality)
        self.assertEquals(0, items[10].quality)
        self.assertEquals(0, items[11].quality)
        self.assertEquals(48, items[12].quality)
        self.assertEquals(47, items[13].quality)
        self.assertEquals(0, items[14].quality)
        self.assertEquals(0, items[15].quality)
        self.assertEquals(46, items[16].quality)
        self.assertEquals(45, items[17].quality)
        self.assertEquals(0, items[18].quality)
        self.assertEquals(0, items[19].quality)
        self.assertEquals(46, items[20].quality)
        self.assertEquals(45, items[21].quality)
        self.assertEquals(0, items[22].quality)
        self.assertEquals(0, items[23].quality)

if __name__ == '__main__':
    unittest.main()
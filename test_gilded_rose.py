import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        name = "foo"
        sell_in = [11, 10, 6, 5, 0, -1]
        quality = [50, 49, 1, 0]
        items = [Item(name, s, q) for s in sell_in for q in quality]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(49, items[0].quality)
        self.assertEquals(48, items[1].quality)
        self.assertEquals(0, items[2].quality)
        self.assertEquals(0, items[3].quality)
        self.assertEquals(49, items[4].quality)
        self.assertEquals(48, items[5].quality)
        self.assertEquals(0, items[6].quality)
        self.assertEquals(0, items[7].quality)
        self.assertEquals(49, items[8].quality)
        self.assertEquals(48, items[9].quality)
        self.assertEquals(0, items[10].quality)
        self.assertEquals(0, items[11].quality)
        self.assertEquals(49, items[12].quality)
        self.assertEquals(48, items[13].quality)
        self.assertEquals(0, items[14].quality)
        self.assertEquals(0, items[15].quality)
        self.assertEquals(48, items[16].quality)
        self.assertEquals(47, items[17].quality)
        self.assertEquals(0, items[18].quality)
        self.assertEquals(0, items[19].quality)
        self.assertEquals(48, items[20].quality)
        self.assertEquals(47, items[21].quality)
        self.assertEquals(0, items[22].quality)
        self.assertEquals(0, items[23].quality)

if __name__ == '__main__':
    unittest.main()
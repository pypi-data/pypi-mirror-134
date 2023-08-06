import unittest

from bdflib import model, effects


class TestEmbolden(unittest.TestCase):
    def _build_test_font(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 1)

        return f

    def test_basic_operation(self):
        f = self._build_test_font()
        f2 = effects.embolden(f)

        self.assertNotEqual(f, f2)

        g = f2[1]
        self.assertEqual(g.bbX, 0)
        self.assertEqual(g.bbY, 0)
        self.assertEqual(g.bbW, 3)
        self.assertEqual(g.bbH, 2)
        self.assertEqual(g.data, [0b110, 0b011])

    def test_maintaining_spacing(self):
        f = effects.embolden(self._build_test_font(), True)

        g = f[1]

        self.assertEqual(g.advance, 4)

    def test_without_maintaining_spacing(self):
        f = effects.embolden(self._build_test_font(), False)

        g = f[1]

        self.assertEqual(g.advance, 3)


class TestMerge(unittest.TestCase):
    def test_basic_operation(self):
        base_font = model.Font(b"BaseFont", 12, 100, 100)
        base_font.new_glyph_from_data(b"base1", [0b10, 0b01], 0, 0, 2, 2, 3, 1)
        base_font.new_glyph_from_data(b"base2", [0b01, 0b10], 0, 0, 2, 2, 3, 2)

        cust_font = model.Font(b"CustomFont", 12, 100, 100)
        cust_font.new_glyph_from_data(b"cust2", [0b1, 0b1], 0, 0, 2, 2, 3, 2)
        cust_font.new_glyph_from_data(b"cust3", [0b1, 0b1], 0, 0, 2, 2, 3, 3)

        # Start by merging the custom font on top of the base font.
        merged1 = effects.merge(base_font, cust_font)

        # We should get an entirely new font.
        self.assertNotEqual(merged1, base_font)
        self.assertNotEqual(merged1, cust_font)

        # The new font should have cust* characters in preference to base
        # characters.
        self.assertEqual(merged1[1].name, b"base1")
        self.assertEqual(merged1[2].name, b"cust2")
        self.assertEqual(merged1[3].name, b"cust3")

        # If we merge things the other way around...
        merged2 = effects.merge(cust_font, base_font)

        # ...the new font should prefer base* characters.
        self.assertEqual(merged2[1].name, b"base1")
        self.assertEqual(merged2[2].name, b"base2")
        self.assertEqual(merged2[3].name, b"cust3")

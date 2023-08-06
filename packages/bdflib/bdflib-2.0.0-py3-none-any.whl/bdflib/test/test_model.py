import unittest

from bdflib import model


class TestFont(unittest.TestCase):
    def test_basic_properties(self):
        f = model.Font(name=b"TestFont", ptSize=12, xdpi=100, ydpi=100)

        # Test that we're storing font fields as attributes.
        self.assertEqual(f.name, b"TestFont")
        self.assertEqual(f.ptSize, 12)
        self.assertEqual(f.xdpi, 100)
        self.assertEqual(f.ydpi, 100)

    def test_property_setting(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        f[b"CHARSET_REGISTRY"] = b"iso8859"
        self.assertEqual(f[b"CHARSET_REGISTRY"], b"iso8859")

    def test_property_iteration(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        self.assertEqual(list(f.property_names()), [])

        f[b"CUSTOM_PROP1"] = b"hello"
        f[b"CUSTOM_PROP2"] = b"world"

        self.assertEqual(
            sorted(f.property_names()),
            [b"CUSTOM_PROP1", b"CUSTOM_PROP2"],
        )

    def test_codepoint_iteration(self):
        f = model.Font(b"TestFont", 12, 100, 100)

        # Add glyphs at code-points out-of-order.
        f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 5)
        f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 16)
        f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 37)
        f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 93)

        codepoints = list(f.codepoints())
        codepoints.sort()

        self.assertEqual(codepoints, [5, 16, 37, 93])

    def test_comments(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        f.add_comment(b"This is another comment")
        f.add_comment(b"hello, world!\nMultiple lines!")
        self.assertEqual(
            f.get_comments(),
            [
                b"This is another comment",
                b"hello, world!",
                b"Multiple lines!",
            ],
        )

    def test_font_copying(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(
            b"TestGlyph",
            [
                0b0001,
                0b0000,
                0b0000,
                0b0000,
                0b0000,
                0b1000,
            ],
            -3,
            -4,
            4,
            6,
            8,
            1,
        )

        f2 = f.copy()
        g2 = f2[1]

        self.assertEqual(g2.name, b"TestGlyph")
        self.assertEqual(
            g2.data,
            [
                0b0001,
                0b0000,
                0b0000,
                0b0000,
                0b0000,
                0b1000,
            ],
        )
        self.assertEqual(g2.get_bounding_box(), (-3, -4, 4, 6))
        self.assertEqual(g2.advance, 8)
        self.assertEqual(g2.codepoint, 1)
        self.assertEqual(f2[g2.codepoint], g2)


class TestGlyph(unittest.TestCase):
    def test_glyph_creation(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(
            b"TestGlyph",
            [
                0b0001,
                0b0000,
                0b0000,
                0b0000,
                0b0000,
                0b1000,
            ],
            -3,
            -4,
            4,
            6,
            8,
            1,
        )

        self.assertEqual(g.name, b"TestGlyph")
        self.assertEqual(
            g.data,
            [
                0b0001,
                0b0000,
                0b0000,
                0b0000,
                0b0000,
                0b1000,
            ],
        )
        self.assertEqual(g.get_bounding_box(), (-3, -4, 4, 6))
        self.assertEqual(g.advance, 8)
        self.assertEqual(g.codepoint, 1)
        self.assertEqual(f[g.codepoint], g)

    def test_duplicate_codepoints(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(b"TestGlyph1", codepoint=1)

        self.assertRaises(
            model.GlyphExists, f.new_glyph_from_data, b"TestGlyph2", codepoint=1
        )

    def test_glyph_merging_no_op(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 1)

        # Draw this glyph onto itself at 0,0
        g.merge_glyph(g, 0, 0)

        # Nothing should have changed.
        self.assertEqual(g.get_bounding_box(), (0, 0, 2, 2))
        self.assertEqual(
            g.data,
            [
                0b10,
                0b01,
            ],
        )

    def test_glyph_merging_above(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 1)

        # Draw this glyph onto itself but a few rows higher.
        g.merge_glyph(g, 0, 4)

        # The bounding box should be higher.
        self.assertEqual(g.get_bounding_box(), (0, 0, 2, 6))

        # There should be some blank rows in the bitmap
        self.assertEqual(
            g.data,
            [
                0b10,
                0b01,
                0b00,
                0b00,
                0b10,
                0b01,
            ],
        )

    def test_glyph_merging_below(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(b"TestGlyph", [0b01, 0b10], 0, 0, 2, 2, 3, 1)

        # Draw this glyph onto itself but a row lower.
        g.merge_glyph(g, 0, -3)

        # The origin vector should have moved downward, and the height
        # increased to compensate.
        self.assertEqual(g.get_bounding_box(), (0, -3, 2, 5))

        # There should be a blank row in the bitmap
        self.assertEqual(
            g.data,
            [
                0b01,
                0b10,
                0b00,
                0b01,
                0b10,
            ],
        )

    def test_glyph_merging_left(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 1)

        # Draw this glyph onto itself a few columns to the left.
        g.merge_glyph(g, -4, 0)

        # The origin vector should have moved left, and the width enlarged to
        # compensate.
        self.assertEqual(g.get_bounding_box(), (-4, 0, 6, 2))

        # The bitmap should be wider.
        self.assertEqual(
            g.data,
            [
                0b100010,
                0b010001,
            ],
        )

    def test_glyph_merging_right(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 1)

        # Draw this glyph onto itself a few columns to the right.
        g.merge_glyph(g, 3, 0)

        # The origin vector should be the same, and the width enlarged.
        self.assertEqual(g.get_bounding_box(), (0, 0, 5, 2))

        # The bitmap should be wider.
        self.assertEqual(
            g.data,
            [
                0b10010,
                0b01001,
            ],
        )

    def test_glyph_merging_offset_glyph(self):
        """
        Merging a glyph whose bitmap doesn't start at (0,0)
        """
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 1, 1, 2, 2, 3, 1)

        # Draw this glyph onto itself to make a diamond.
        g.merge_glyph(g, -1, 1)

        # The origin vector should be the same, and the width enlarged.
        self.assertEqual(g.get_bounding_box(), (0, 1, 3, 3))

        # The bitmap should be a larger diagonal.
        self.assertEqual(
            g.data,
            [
                0b010,
                0b101,
                0b010,
            ],
        )

    def test_glyph_merging(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 1)

        # Draw this glyph onto itself at 2,2
        g.merge_glyph(g, 2, 2)

        # Check the results
        self.assertEqual(g.get_bounding_box(), (0, 0, 4, 4))
        self.assertEqual(
            g.data,
            [
                0b1000,
                0b0100,
                0b0010,
                0b0001,
            ],
        )

    def test_glyph_printing(self):

        # A small circle
        glyph_data = [
            0b01110,
            0b10001,
            0b10001,
            0b10001,
            0b01110,
        ]

        f = model.Font(b"TestFont", 12, 100, 100)
        glyphs = []
        for offset in range(0, 7):
            glyphs.append(
                f.new_glyph_from_data(
                    b"TestGlyph%d" % offset,
                    glyph_data,
                    -5 + offset,
                    -5 + offset,
                    5,
                    5,
                    offset,
                    offset,
                )
            )

        for g in glyphs:
            print(g)
            print()

        self.assertEqual(
            [str(g) for g in glyphs],
            [
                "-----+\n.###.|\n#...#|\n#...#|\n#...#|\n.###.|",
                "-###+\n#...#\n#...#\n#...#\n.###|",
                ".###.\n#--+#\n#..|#\n#..|#\n.###.",
                ".###.\n#.|.#\n#-+-#\n#.|.#\n.###.",
                ".###.\n#|..#\n#|..#\n#+--#\n.###.",
                "|###.\n#...#\n#...#\n#...#\n+###-",
                "|.###.\n|#...#\n|#...#\n|#...#\n|.###.\n+-----",
            ],
        )

    def test_glyph_get_ascent_and_descent(self):
        f = model.Font(b"TestFont", 12, 100, 100)

        # For a simple glyph at the origin, ascent and descent should match the
        # bitmap bounding box.
        g = f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 1)
        self.assertEqual(g.get_ascent(), 2)
        self.assertEqual(g.get_descent(), 0)

        # If the bitmap crosses the baseline, we should get a positive ascent
        # and descent.
        g = f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, -1, 2, 2, 3, 2)
        self.assertEqual(g.get_ascent(), 1)
        self.assertEqual(g.get_descent(), 1)

        # If the bitmap is well above the baseline, ascent should be positive
        # and descent negative.
        g = f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, 1, 2, 2, 3, 3)
        self.assertEqual(g.get_ascent(), 3)
        self.assertEqual(g.get_descent(), -1)

        # If the bitmap is well below the baseline, ascent should be negative
        # and descent positive.
        g = f.new_glyph_from_data(b"TestGlyph", [0b10, 0b01], 0, -3, 2, 2, 3, 4)
        self.assertEqual(g.get_ascent(), -1)
        self.assertEqual(g.get_descent(), 3)

        # Ascent and descent should be calculated from the actual extents of
        # the character, not the bitmap.

        g = f.new_glyph_from_data(
            b"TestGlyph", [0b00, 0b10, 0b01, 0b00], 0, -2, 2, 4, 3, 5
        )
        self.assertEqual(g.get_ascent(), 1)
        self.assertEqual(g.get_descent(), 1)

    def test_iter_pixels(self):
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(
            name=b"LATIN SMALL LETTER H",
            data=[0b101, 0b111, 0b100],
            bbX=0,
            bbY=0,
            bbW=3,
            bbH=3,
            advance=4,
            codepoint=ord("h"),
        )

        pixels = [list(row) for row in g.iter_pixels()]

        self.assertEqual(
            pixels,
            [
                [True, False, False],
                [True, True, True],
                [True, False, True],
            ],
        )

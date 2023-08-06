import unittest

from io import BytesIO

from bdflib import model, reader

# This comes from the X11 BDF spec.
SAMPLE_FONT = b"""
STARTFONT 2.1
COMMENT This is a sample font in 2.1 format.
FONT -Adobe-Helvetica-Bold-R-Normal--24-240-75-75-P-65-ISO8859-1
SIZE 24 75 75
FONTBOUNDINGBOX 9 24 -2 -6
STARTPROPERTIES 19
FOUNDRY "Adobe"
FAMILY "Helvetica"
WEIGHT_NAME "Bold"
SLANT "R"
SETWIDTH_NAME "Normal"
ADD_STYLE_NAME ""
PIXEL_SIZE 24
POINT_SIZE 240
RESOLUTION_X 75
RESOLUTION_Y 75
SPACING "P"
AVERAGE_WIDTH 65
CHARSET_REGISTRY "ISO8859"
CHARSET_ENCODING "1"
MIN_SPACE 4
FONT_ASCENT 21
FONT_DESCENT 7
COPYRIGHT "Copyright (c) 1987 Adobe Systems, Inc."
NOTICE "Helvetica is a registered trademark of Linotype Inc."
ENDPROPERTIES
CHARS 2
STARTCHAR j
ENCODING 106
SWIDTH 355 0
DWIDTH 8 0
BBX 9 22 -2 -6
BITMAP
0380
0380
0380
0380
0000
0700
0700
0700
0700
0E00
0E00
0E00
0E00
0E00
1C00
1C00
1C00
1C00
3C00
7800
F000
E000
ENDCHAR
STARTCHAR quoteright
ENCODING 39
SWIDTH 223 0
DWIDTH 5 0
BBX 4 6 2 12
ATTRIBUTES 01C0
BITMAP
70
70
70
60
E0
C0
ENDCHAR
ENDFONT
""".strip()


class TestGlyph(unittest.TestCase):
    def test_basic_operation(self):
        testFont = model.Font(b"Adobe Helvetica", 24, 75, 75)
        testComments = []
        testGlyphData = reader._next_token(
            SAMPLE_FONT.split(b"\n")[27:56], testComments
        )

        reader._read_glyph(testGlyphData, testFont)

        # The font should now have an entry for j.
        testGlyph = testFont[106]

        # The glyph should have the correct header data.
        self.assertEqual(testGlyph.name, b"j")
        self.assertEqual(testGlyph.codepoint, 106)
        self.assertEqual(testGlyph.advance, 8)
        self.assertEqual(testGlyph.bbX, -2)
        self.assertEqual(testGlyph.bbY, -6)
        self.assertEqual(testGlyph.bbW, 9)
        self.assertEqual(testGlyph.bbH, 22)

        # Make sure we got the correct glyph bitmap.
        self.assertEqual(
            str(testGlyph),
            "..|...###\n"
            "..|...###\n"
            "..|...###\n"
            "..|...###\n"
            "..|......\n"
            "..|..###.\n"
            "..|..###.\n"
            "..|..###.\n"
            "..|..###.\n"
            "..|.###..\n"
            "..|.###..\n"
            "..|.###..\n"
            "..|.###..\n"
            "..|.###..\n"
            "..|###...\n"
            "--+###---\n"
            "..|###...\n"
            "..|###...\n"
            "..####...\n"
            ".####....\n"
            "####.....\n"
            "###......",
        )

        # The iterator should have nothing left in it.
        self.assertRaises(StopIteration, next, testGlyphData)


class TestReadProperty(unittest.TestCase):
    def test_basic_operation(self):
        testFont = model.Font(b"Adobe Helvetica", 24, 75, 75)
        testComments = []
        testProperties = reader._next_token(
            SAMPLE_FONT.split(b"\n")[6:26], testComments
        )

        for i in range(19):
            key, value = next(testProperties)
            testFont[key] = reader._unquote_property_value(value)

        # After reading the properties, the iterator should be just up to the
        # ENDPROPERTIES line.
        self.assertEqual(next(testProperties)[0], b"ENDPROPERTIES")

        # Test that the properties were read correctly.
        self.assertEqual(testFont[b"FOUNDRY"], b"Adobe")
        self.assertEqual(testFont[b"FAMILY"], b"Helvetica")
        self.assertEqual(testFont[b"WEIGHT_NAME"], b"Bold")
        self.assertEqual(testFont[b"SLANT"], b"R")
        self.assertEqual(testFont[b"SETWIDTH_NAME"], b"Normal")
        self.assertEqual(testFont[b"ADD_STYLE_NAME"], b"")
        self.assertEqual(testFont[b"POINT_SIZE"], 240)
        self.assertEqual(testFont[b"RESOLUTION_X"], 75)
        self.assertEqual(testFont[b"RESOLUTION_Y"], 75)
        self.assertEqual(testFont[b"SPACING"], b"P")
        self.assertEqual(testFont[b"AVERAGE_WIDTH"], 65)
        self.assertEqual(testFont[b"CHARSET_REGISTRY"], b"ISO8859")
        self.assertEqual(testFont[b"CHARSET_ENCODING"], b"1")
        self.assertEqual(testFont[b"MIN_SPACE"], 4)
        self.assertEqual(testFont[b"FONT_ASCENT"], 21)
        self.assertEqual(testFont[b"FONT_DESCENT"], 7)
        self.assertEqual(
            testFont[b"COPYRIGHT"], b"Copyright (c) 1987 Adobe Systems, Inc."
        )
        self.assertEqual(
            testFont[b"NOTICE"],
            b"Helvetica is a registered trademark of Linotype Inc.",
        )
        self.assertEqual(testComments, [])


class TestReadFont(unittest.TestCase):
    def _check_font(self, font):
        """
        Checks that the given font is a representation of the sample font.
        """
        self.assertEqual(
            font.name,
            b"-Adobe-Helvetica-Bold-R-Normal--24-240-75-75-P-65-ISO8859-1",
        )
        self.assertEqual(font.ptSize, 24.0)
        self.assertEqual(font.xdpi, 75)
        self.assertEqual(font.ydpi, 75)
        self.assertEqual(
            font.get_comments(), [b"This is a sample font in 2.1 format."]
        )
        self.assertEqual(len(font.glyphs), 2)
        # Our code ignores PIXEL_SIZE but adds FACE_NAME, so the total is still
        # 19.
        self.assertEqual(len(font.properties), 19)

    def test_basic_operation(self):
        testFontData = BytesIO(SAMPLE_FONT)
        testFont = reader.read_bdf(testFontData)

        self._check_font(testFont)

    def test_extra_blank_lines(self):
        """
        We should ignore any extra lines in the input.
        """
        testFontData = BytesIO(SAMPLE_FONT.replace(b"\n", b"\n\n"))
        testFont = reader.read_bdf(testFontData)

        self._check_font(testFont)

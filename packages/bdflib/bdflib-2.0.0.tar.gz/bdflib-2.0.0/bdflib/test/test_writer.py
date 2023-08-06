import unittest
from io import BytesIO

from bdflib import model, writer


class TestBDFWriter(unittest.TestCase):
    def setUp(self):
        self.font = model.Font(b"TestFont", 12, 100, 100)

    def test_basic_writing(self):
        """
        Writing out a simple font should work.
        """
        self.font.new_glyph_from_data(
            b"TestGlyph", [0b10, 0b01], 0, 0, 2, 2, 3, 1
        )

        stream = BytesIO()
        writer.write_bdf(self.font, stream)

        self.assertEqual(
            stream.getvalue().decode("UTF-8"),
            "STARTFONT 2.1\n"
            "FONT TestFont\n"
            "SIZE 12 100 100\n"
            "FONTBOUNDINGBOX 2 2 0 0\n"
            "STARTPROPERTIES 0\n"
            "ENDPROPERTIES\n"
            "CHARS 1\n"
            "STARTCHAR TestGlyph\n"
            "ENCODING 1\n"
            "SWIDTH 176 0\n"
            "DWIDTH 3 0\n"
            "BBX 2 2 0 0\n"
            "BITMAP\n"
            "40\n"
            "80\n"
            "ENDCHAR\n"
            "ENDFONT\n",
        )

    def test_empty_font(self):
        """
        We should be able to write an empty font.
        """
        stream = BytesIO()
        writer.write_bdf(self.font, stream)

        self.assertEqual(
            stream.getvalue().decode("UTF-8"),
            "STARTFONT 2.1\n"
            "FONT TestFont\n"
            "SIZE 12 100 100\n"
            "FONTBOUNDINGBOX 0 0 0 0\n"
            "STARTPROPERTIES 0\n"
            "ENDPROPERTIES\n"
            "CHARS 0\n"
            "ENDFONT\n",
        )

    def test_bounding_box_calculations(self):
        """
        FONTBOUNDINGBOX should be calculated from individual glyphs.
        """
        self.font.new_glyph_from_data(
            b"TestGlyph1", [0b10, 0b01], 1, 3, 2, 2, 3, 1
        )
        self.font.new_glyph_from_data(
            b"TestGlyph2", [0b10, 0b01], -5, -7, 2, 2, 1, 2
        )

        stream = BytesIO()
        writer.write_bdf(self.font, stream)

        self.assertEqual(
            stream.getvalue().decode("UTF-8"),
            "STARTFONT 2.1\n"
            "FONT TestFont\n"
            "SIZE 12 100 100\n"
            "FONTBOUNDINGBOX 8 12 -5 -7\n"
            "STARTPROPERTIES 0\n"
            "ENDPROPERTIES\n"
            "CHARS 2\n"
            "STARTCHAR TestGlyph1\n"
            "ENCODING 1\n"
            "SWIDTH 176 0\n"
            "DWIDTH 3 0\n"
            "BBX 2 2 1 3\n"
            "BITMAP\n"
            "40\n"
            "80\n"
            "ENDCHAR\n"
            "STARTCHAR TestGlyph2\n"
            "ENCODING 2\n"
            "SWIDTH 58 0\n"
            "DWIDTH 1 0\n"
            "BBX 2 2 -5 -7\n"
            "BITMAP\n"
            "40\n"
            "80\n"
            "ENDCHAR\n"
            "ENDFONT\n",
        )

    def test_property_quoting(self):
        """
        Test that property values are quoted properly.
        """

        self.font[b"AN_INTEGER"] = 42
        self.font[b"A_STRING"] = b"42"
        self.font[b"STRING_WITH_QUOTES"] = b'Neville "The Banker" Robinson'

        stream = BytesIO()
        writer.write_bdf(self.font, stream)

        self.assertEqual(
            stream.getvalue().decode("UTF-8"),
            "STARTFONT 2.1\n"
            "FONT TestFont\n"
            "SIZE 12 100 100\n"
            "FONTBOUNDINGBOX 0 0 0 0\n"
            "STARTPROPERTIES 3\n"
            "AN_INTEGER 42\n"
            'A_STRING "42"\n'
            'STRING_WITH_QUOTES "Neville ""The Banker"" Robinson"\n'
            "ENDPROPERTIES\n"
            "CHARS 0\n"
            "ENDFONT\n",
        )

    def test_default_char_setting(self):
        """
        If a default char is explicitly set, it should be used.
        """
        self.font.new_glyph_from_data(
            b"TestGlyph1", [0b10, 0b01], 0, 0, 2, 2, 3, 1
        )
        self.font.new_glyph_from_data(
            b"TestGlyph2", [0b01, 0b10], 0, 0, 2, 2, 3, 0xFFFD
        )
        self.font[b"DEFAULT_CHAR"] = 0xFFFD

        stream = BytesIO()
        writer.write_bdf(self.font, stream)

        self.assertEqual(
            stream.getvalue().decode("UTF-8"),
            "STARTFONT 2.1\n"
            "FONT TestFont\n"
            "SIZE 12 100 100\n"
            "FONTBOUNDINGBOX 2 2 0 0\n"
            "STARTPROPERTIES 1\n"
            "DEFAULT_CHAR 65533\n"
            "ENDPROPERTIES\n"
            "CHARS 2\n"
            "STARTCHAR TestGlyph1\n"
            "ENCODING 1\n"
            "SWIDTH 176 0\n"
            "DWIDTH 3 0\n"
            "BBX 2 2 0 0\n"
            "BITMAP\n"
            "40\n"
            "80\n"
            "ENDCHAR\n"
            "STARTCHAR TestGlyph2\n"
            "ENCODING 65533\n"
            "SWIDTH 176 0\n"
            "DWIDTH 3 0\n"
            "BBX 2 2 0 0\n"
            "BITMAP\n"
            "80\n"
            "40\n"
            "ENDCHAR\n"
            "ENDFONT\n",
        )

    def test_resolution_calculations(self):
        """
        The pixel size should be correctly calculated from the point size.
        """
        tests = [
            (12, 72, 12),
            (12, 100, 17),
            (12.2, 100, 17),
            (12, 144, 24),
        ]

        for pointSz, res, pixelSz in tests:
            deci_pointSz = int(pointSz * 10)

            font = model.Font(b"TestFont", pointSz, res, res)

            stream = BytesIO()
            writer.write_bdf(font, stream)

            self.assertEqual(
                stream.getvalue().decode("UTF-8"),
                "STARTFONT 2.1\n"
                "FONT TestFont\n"
                "SIZE %(pointSz)g %(res)d %(res)d\n"
                "FONTBOUNDINGBOX 0 0 0 0\n"
                "STARTPROPERTIES 0\n"
                "ENDPROPERTIES\n"
                "CHARS 0\n"
                "ENDFONT\n"
                % {
                    "pointSz": pointSz,
                    "res": res,
                    "pixelSz": pixelSz,
                    "deci_pointSz": deci_pointSz,
                },
            )

    def test_glyph_data_case(self):
        """
        gbdfed writes upper-case hex digits, so we should too.
        """
        f = model.Font(b"TestFont", 12, 100, 100)
        g = f.new_glyph_from_data(
            b"TestGlyph",
            [0xA, 0xB, 0xC, 0xD, 0xE, 0xF],
            bbW=4,
            bbH=6,
            advance=5,
        )

        stream = BytesIO()
        writer.write_bdf(f, stream)

        self.assertEqual(
            stream.getvalue().decode("UTF-8"),
            "STARTFONT 2.1\n"
            "FONT TestFont\n"
            "SIZE 12 100 100\n"
            "FONTBOUNDINGBOX 4 6 0 0\n"
            "STARTPROPERTIES 0\n"
            "ENDPROPERTIES\n"
            "CHARS 1\n"
            "STARTCHAR TestGlyph\n"
            "ENCODING -1\n"
            "SWIDTH 294 0\n"
            "DWIDTH 5 0\n"
            "BBX 4 6 0 0\n"
            "BITMAP\n"
            "F0\n"
            "E0\n"
            "D0\n"
            "C0\n"
            "B0\n"
            "A0\n"
            "ENDCHAR\n"
            "ENDFONT\n",
        )

    def test_glyphs_should_be_zero_padded(self):
        """
        Each row of the bitmap should be zero-padded to the same length.
        """
        f = model.Font(b"TestFont", 12, 100, 100)

        # When a glyph is multiple hex-digits wide and a row has no bits set in
        # the left-most columns, a zero should be placed there.
        g = f.new_glyph_from_data(
            b"TestGlyph", [0b100000000000, 0b1], bbW=12, bbH=2
        )

        stream = BytesIO()
        writer.write_bdf(f, stream)

        self.assertEqual(
            stream.getvalue().decode("UTF-8"),
            "STARTFONT 2.1\n"
            "FONT TestFont\n"
            "SIZE 12 100 100\n"
            "FONTBOUNDINGBOX 12 2 0 0\n"
            "STARTPROPERTIES 0\n"
            "ENDPROPERTIES\n"
            "CHARS 1\n"
            "STARTCHAR TestGlyph\n"
            "ENCODING -1\n"
            "SWIDTH 0 0\n"
            "DWIDTH 0 0\n"
            "BBX 12 2 0 0\n"
            "BITMAP\n"
            "0010\n"
            "8000\n"
            "ENDCHAR\n"
            "ENDFONT\n",
        )

        # When a glyph's width doesn't take up a even number of hex digits, the
        # row width should be rounded up to the nearest even number of
        # digits, not down.
        g = f.new_glyph_from_data(
            b"TestGlyph", [0b10000000000, 0b00000001000], bbW=11, bbH=2
        )

        stream = BytesIO()
        writer.write_bdf(f, stream)

        self.assertEqual(
            stream.getvalue().decode("UTF-8"),
            "STARTFONT 2.1\n"
            "FONT TestFont\n"
            "SIZE 12 100 100\n"
            "FONTBOUNDINGBOX 12 2 0 0\n"
            "STARTPROPERTIES 0\n"
            "ENDPROPERTIES\n"
            "CHARS 2\n"
            "STARTCHAR TestGlyph\n"
            "ENCODING -1\n"
            "SWIDTH 0 0\n"
            "DWIDTH 0 0\n"
            "BBX 12 2 0 0\n"
            "BITMAP\n"
            "0010\n"
            "8000\n"
            "ENDCHAR\n"
            "STARTCHAR TestGlyph\n"
            "ENCODING -1\n"
            "SWIDTH 0 0\n"
            "DWIDTH 0 0\n"
            "BBX 11 2 0 0\n"
            "BITMAP\n"
            "0100\n"
            "8000\n"
            "ENDCHAR\n"
            "ENDFONT\n",
        )

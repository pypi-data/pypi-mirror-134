import unittest

from bdflib import model, xlfd

FONTNAME = b"-screwtapello-testfont-medium-r-normal--5-50-75-75-m-45-iso10646-1"


class TestFix(unittest.TestCase):
    def test_set_xlfd_properties_from_bdf_fields(self) -> None:
        """
        xlfd.fix() calculates all the properties that can be calculated.
        """
        f = model.Font(name=FONTNAME, ptSize=5, xdpi=75, ydpi=75)
        f.new_glyph_from_data(
            name="j",
            data=[
                0b10,
                0b01,
                0b01,
                0b01,
                0b00,
                0b01,
            ],
            bbX=0,
            bbY=-1,
            bbW=2,
            bbH=6,
            advance=3,
            codepoint=ord("j"),
        )
        f.new_glyph_from_data(
            name="m",
            data=[
                0b1001001,
                0b1001001,
                0b0110110,
            ],
            bbX=0,
            bbY=0,
            bbW=7,
            bbH=3,
            advance=8,
            codepoint=ord("m"),
        )

        # Fix/generate as much information as possible.
        xlfd.fix(f)

        self.assertEqual(f[xlfd.WEIGHT_NAME], b"Medium")
        self.assertEqual(f[xlfd.SLANT], xlfd.SLANT_ROMAN)
        self.assertEqual(f[xlfd.SETWIDTH_NAME], b"Normal")
        self.assertEqual(f[xlfd.ADD_STYLE_NAME], b"")
        self.assertEqual(f[xlfd.PIXEL_SIZE], 6)
        self.assertEqual(f[xlfd.POINT_SIZE], 50)
        self.assertEqual(f[xlfd.RESOLUTION_X], 75)
        self.assertEqual(f[xlfd.RESOLUTION_Y], 75)
        self.assertEqual(f[xlfd.SPACING], xlfd.SPACING_PROPORTIONAL)
        self.assertEqual(f[xlfd.AVERAGE_WIDTH], 55)
        self.assertEqual(f[xlfd.FONT_ASCENT], 5)
        self.assertEqual(f[xlfd.FONT_DESCENT], 1)
        self.assertEqual(f[xlfd.DEFAULT_CHAR], ord("m"))

    def test_detect_charcell_spacing(self) -> None:
        """
        xlfd.fix() detects when a font uses charcell spacing..
        """
        f = model.Font(name=FONTNAME, ptSize=5, xdpi=75, ydpi=75)

        # Add glyphs that both have the same advance width,
        # and don't draw outside their cell.
        f.new_glyph_from_data(
            name="j",
            data=[
                0b01110,
                0b10001,
                0b00001,
                0b00111,
                0b00000,
                0b00001,
            ],
            bbX=0,
            bbY=-1,
            bbW=5,
            bbH=6,
            advance=6,
            codepoint=ord("j"),
        )
        f.new_glyph_from_data(
            name="m",
            data=[
                0b10101,
                0b10101,
                0b01010,
            ],
            bbX=0,
            bbY=0,
            bbW=5,
            bbH=3,
            advance=6,
            codepoint=ord("m"),
        )

        # Fix/generate as much information as possible.
        xlfd.fix(f)

        self.assertEqual(f[xlfd.SPACING], xlfd.SPACING_CHARCELL)

    def test_detect_monospace_spacing(self) -> None:
        """
        xlfd.fix() detects when a font uses monospace spacing..
        """
        f = model.Font(name=FONTNAME, ptSize=5, xdpi=75, ydpi=75)

        # Add glyphs that both have the same advance width,
        # but may draw outside their cell.
        f.new_glyph_from_data(
            name="j",
            data=[
                0b01110,
                0b10001,
                0b00001,
                0b00111,
                0b00000,
                0b00001,
            ],
            bbX=0,
            bbY=-1,
            bbW=5,
            bbH=6,
            advance=6,
            codepoint=ord("j"),
        )
        f.new_glyph_from_data(
            name="m",
            data=[
                0b010101,
                0b010101,
                0b101010,
            ],
            bbX=-1,
            bbY=0,
            bbW=6,
            bbH=3,
            advance=6,
            codepoint=ord("m"),
        )

        # Fix/generate as much information as possible.
        xlfd.fix(f)

        self.assertEqual(f[xlfd.SPACING], xlfd.SPACING_MONOSPACED)

    def test_respect_existing_properties(self) -> None:
        """
        xlfd.fix() does not overwrite previously-set properties.
        """
        f = model.Font(name=FONTNAME, ptSize=5, xdpi=75, ydpi=75)
        f.new_glyph_from_data(
            name="j",
            data=[
                0b10,
                0b01,
                0b01,
                0b01,
                0b00,
                0b01,
            ],
            bbX=0,
            bbY=-1,
            bbW=2,
            bbH=6,
            advance=3,
            codepoint=ord("j"),
        )
        f.new_glyph_from_data(
            name="m",
            data=[
                0b1001001,
                0b1001001,
                0b0110110,
            ],
            bbX=0,
            bbY=0,
            bbW=7,
            bbH=3,
            advance=8,
            codepoint=ord("m"),
        )

        f[xlfd.WEIGHT_NAME] = b"Thin"
        f[xlfd.SLANT] = xlfd.SLANT_REVERSE_OBLIQUE
        f[xlfd.SETWIDTH_NAME] = b"Ultracondensed"
        f[xlfd.ADD_STYLE_NAME] = b"Loopy"
        f[xlfd.PIXEL_SIZE] = 10
        f[xlfd.POINT_SIZE] = 100
        f[xlfd.RESOLUTION_X] = 96
        f[xlfd.RESOLUTION_Y] = 12
        f[xlfd.SPACING] = xlfd.SPACING_CHARCELL
        f[xlfd.AVERAGE_WIDTH] = 993
        f[xlfd.FONT_ASCENT] = 123
        f[xlfd.FONT_DESCENT] = 456
        f[xlfd.DEFAULT_CHAR] = ord("j")

        # Fix/generate as much information as possible.
        xlfd.fix(f)

        self.assertEqual(f[xlfd.WEIGHT_NAME], b"Thin")
        self.assertEqual(f[xlfd.SLANT], xlfd.SLANT_REVERSE_OBLIQUE)
        self.assertEqual(f[xlfd.SETWIDTH_NAME], b"Ultracondensed")
        self.assertEqual(f[xlfd.ADD_STYLE_NAME], b"Loopy")
        self.assertEqual(f[xlfd.PIXEL_SIZE], 10)
        self.assertEqual(f[xlfd.POINT_SIZE], 100)
        self.assertEqual(f[xlfd.RESOLUTION_X], 96)
        self.assertEqual(f[xlfd.RESOLUTION_Y], 12)
        self.assertEqual(f[xlfd.SPACING], xlfd.SPACING_CHARCELL)
        self.assertEqual(f[xlfd.AVERAGE_WIDTH], 993)
        self.assertEqual(f[xlfd.FONT_ASCENT], 123)
        self.assertEqual(f[xlfd.FONT_DESCENT], 456)
        self.assertEqual(f[xlfd.DEFAULT_CHAR], ord("j"))


class TestValidate(unittest.TestCase):
    """
    Validation rules from Chapter 8 of the XLFD specification.
    """

    def test_reject_if_name_not_xlfd(self) -> None:
        """
        xlfd.validate() rejects a font whose name is not an XLFD name.
        """
        f = model.Font(name=b"invalid xlfd", ptSize=5, xdpi=75, ydpi=75)
        errors = xlfd.validate(f)
        self.assertIn(xlfd.NotAnXlfd(b"invalid xlfd"), errors)

    def test_reject_if_name_includes_invalid_characters(self) -> None:
        """
        xlfd.validate() rejects a font whose name includes invalid characters.
        """

        for c in (b"-", b"?", b"*", b",", b'"'):
            invalid_font_name = FONTNAME + c
            f = model.Font(name=invalid_font_name, ptSize=5, xdpi=75, ydpi=75)
            errors = xlfd.validate(f)
            self.assertIn(xlfd.NotAnXlfd(invalid_font_name), errors)

    def test_accept_valid_name(self) -> None:
        """
        xlfd.validate() does not complain about a valid XLFD name.
        """
        f = model.Font(name=FONTNAME, ptSize=5, xdpi=75, ydpi=75)
        errors = xlfd.validate(f)
        self.assertNotIn(xlfd.NotAnXlfd(FONTNAME), errors)

    def test_reject_if_missing_property_values(self) -> None:
        """
        xlfd.validate() requires all FontName properties to be present.
        """
        f = model.Font(name=FONTNAME, ptSize=5, xdpi=75, ydpi=75)
        errors = xlfd.validate(f)
        self.assertIn(xlfd.MissingProperty(xlfd.FOUNDRY), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.FAMILY_NAME), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.WEIGHT_NAME), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.SLANT), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.SETWIDTH_NAME), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.ADD_STYLE_NAME), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.PIXEL_SIZE), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.POINT_SIZE), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.RESOLUTION_X), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.RESOLUTION_Y), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.SPACING), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.AVERAGE_WIDTH), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.CHARSET_REGISTRY), errors)
        self.assertIn(xlfd.MissingProperty(xlfd.CHARSET_ENCODING), errors)

    def test_reject_if_xlfd_property_mismatch(self) -> None:
        """
        xlfd.validate() requires XLFD field values match the font properties.
        """
        f = model.Font(name=FONTNAME, ptSize=5, xdpi=75, ydpi=75)

        f[xlfd.FOUNDRY] = b"a"
        f[xlfd.FAMILY_NAME] = b"b"
        f[xlfd.WEIGHT_NAME] = b"Thin"
        f[xlfd.SLANT] = xlfd.SLANT_REVERSE_OBLIQUE
        f[xlfd.SETWIDTH_NAME] = b"Condensed"
        f[xlfd.ADD_STYLE_NAME] = b"Loopy"
        f[xlfd.PIXEL_SIZE] = 10
        f[xlfd.POINT_SIZE] = 100
        f[xlfd.RESOLUTION_X] = 96
        f[xlfd.RESOLUTION_Y] = 12
        f[xlfd.SPACING] = xlfd.SPACING_CHARCELL
        f[xlfd.AVERAGE_WIDTH] = 993
        f[xlfd.CHARSET_REGISTRY] = b"iso8859"
        f[xlfd.CHARSET_ENCODING] = b"15"

        errors = xlfd.validate(f)

        self.assertIn(
            xlfd.Contradiction(xlfd.FOUNDRY, b"a", b"screwtapello"), errors
        )
        self.assertIn(
            xlfd.Contradiction(xlfd.FAMILY_NAME, b"b", b"testfont"), errors
        )
        self.assertIn(
            xlfd.Contradiction(xlfd.WEIGHT_NAME, b"Thin", b"medium"), errors
        )
        self.assertIn(
            xlfd.Contradiction(
                xlfd.SLANT, xlfd.SLANT_REVERSE_OBLIQUE, xlfd.SLANT_ROMAN
            ),
            errors,
        )
        self.assertIn(
            xlfd.Contradiction(xlfd.SETWIDTH_NAME, b"Condensed", b"normal"),
            errors,
        )
        self.assertIn(
            xlfd.Contradiction(xlfd.ADD_STYLE_NAME, b"Loopy", b""), errors
        )
        self.assertIn(xlfd.Contradiction(xlfd.PIXEL_SIZE, 10, 5), errors)
        self.assertIn(xlfd.Contradiction(xlfd.POINT_SIZE, 100, 50), errors)
        self.assertIn(xlfd.Contradiction(xlfd.RESOLUTION_X, 96, 75), errors)
        self.assertIn(xlfd.Contradiction(xlfd.RESOLUTION_Y, 12, 75), errors)
        self.assertIn(
            xlfd.Contradiction(
                xlfd.SPACING, xlfd.SPACING_CHARCELL, xlfd.SPACING_MONOSPACED
            ),
            errors,
        )
        self.assertIn(xlfd.Contradiction(xlfd.AVERAGE_WIDTH, 993, 45), errors)
        self.assertIn(
            xlfd.Contradiction(xlfd.CHARSET_REGISTRY, b"iso8859", b"iso10646"),
            errors,
        )
        self.assertIn(
            xlfd.Contradiction(xlfd.CHARSET_ENCODING, b"15", b"1"), errors
        )

    def test_reject_if_invalid_property_values(self) -> None:
        """
        xlfd.validate() requires all properties have the expected types.
        """
        f = model.Font(name=FONTNAME, ptSize=5, xdpi=75, ydpi=75)
        f.new_glyph_from_data(
            name="j",
            data=[
                0b10,
                0b01,
                0b01,
                0b01,
                0b00,
                0b01,
            ],
            bbX=0,
            bbY=-1,
            bbW=2,
            bbH=6,
            advance=3,
            codepoint=ord("j"),
        )

        f[xlfd.FOUNDRY] = 123
        f[xlfd.FAMILY_NAME] = 456
        f[xlfd.WEIGHT_NAME] = 789
        f[xlfd.SLANT] = b"invalid"
        f[xlfd.SETWIDTH_NAME] = 101112
        f[xlfd.ADD_STYLE_NAME] = 131415
        f[xlfd.PIXEL_SIZE] = b"pixel size"
        f[xlfd.POINT_SIZE] = b"point size"
        f[xlfd.RESOLUTION_X] = b"resolution x"
        f[xlfd.RESOLUTION_Y] = b"resolution y"
        f[xlfd.SPACING] = b"invalid"
        f[xlfd.AVERAGE_WIDTH] = b"average width"
        f[xlfd.CHARSET_REGISTRY] = 161718
        f[xlfd.CHARSET_ENCODING] = 192021
        f[xlfd.FONT_ASCENT] = b"invalid"
        f[xlfd.FONT_DESCENT] = b"invalid"
        f[xlfd.DEFAULT_CHAR] = ord("m")

        errors = xlfd.validate(f)

        self.assertIn(xlfd.ExpectedBytestring(xlfd.FOUNDRY, 123), errors)
        self.assertIn(xlfd.ExpectedBytestring(xlfd.FAMILY_NAME, 456), errors)
        self.assertIn(xlfd.ExpectedBytestring(xlfd.WEIGHT_NAME, 789), errors)
        self.assertIn(
            xlfd.ExpectedEnumeratedValue(
                xlfd.SLANT, b"invalid", xlfd.SLANT_VALUES
            ),
            errors,
        )
        self.assertIn(
            xlfd.ExpectedBytestring(xlfd.SETWIDTH_NAME, 101112), errors
        )
        self.assertIn(
            xlfd.ExpectedBytestring(xlfd.ADD_STYLE_NAME, 131415), errors
        )
        self.assertIn(
            xlfd.ExpectedInteger(xlfd.PIXEL_SIZE, b"pixel size"), errors
        )
        self.assertIn(
            xlfd.ExpectedInteger(xlfd.POINT_SIZE, b"point size"), errors
        )
        self.assertIn(
            xlfd.ExpectedInteger(xlfd.RESOLUTION_X, b"resolution x"), errors
        )
        self.assertIn(
            xlfd.ExpectedInteger(xlfd.RESOLUTION_Y, b"resolution y"), errors
        )
        self.assertIn(
            xlfd.ExpectedEnumeratedValue(
                xlfd.SPACING, b"invalid", xlfd.SPACING_VALUES
            ),
            errors,
        )
        self.assertIn(
            xlfd.ExpectedInteger(xlfd.AVERAGE_WIDTH, b"average width"), errors
        )
        self.assertIn(
            xlfd.ExpectedBytestring(xlfd.CHARSET_REGISTRY, 161718), errors
        )
        self.assertIn(
            xlfd.ExpectedBytestring(xlfd.CHARSET_ENCODING, 192021), errors
        )
        self.assertIn(
            xlfd.ExpectedInteger(xlfd.FONT_ASCENT, b"invalid"), errors
        )
        self.assertIn(
            xlfd.ExpectedInteger(xlfd.FONT_DESCENT, b"invalid"), errors
        )
        self.assertIn(
            xlfd.ExpectedEnumeratedValue(
                xlfd.DEFAULT_CHAR, ord("m"), {ord("j")}
            ),
            errors,
        )

        # Check that enumerated properties with the wrong type,
        # not just an invalid value,
        # are also detected.
        f = model.Font(name=FONTNAME, ptSize=5, xdpi=75, ydpi=75)
        f[xlfd.SLANT] = 123
        f[xlfd.SPACING] = 456
        f[xlfd.DEFAULT_CHAR] = b"invalid"

        errors = xlfd.validate(f)

        self.assertIn(
            xlfd.ExpectedEnumeratedValue(xlfd.SLANT, 123, xlfd.SLANT_VALUES),
            errors,
        )
        self.assertIn(
            xlfd.ExpectedEnumeratedValue(
                xlfd.SPACING, 456, xlfd.SPACING_VALUES
            ),
            errors,
        )
        self.assertIn(
            xlfd.ExpectedEnumeratedValue(xlfd.DEFAULT_CHAR, b"invalid", set()),
            errors,
        )

    def test_accept_clean_font(self) -> None:
        """
        xlfd.validate() accepts a font that passes all its tests.
        """
        f = model.Font(name=FONTNAME, ptSize=5, xdpi=75, ydpi=75)

        f[xlfd.FOUNDRY] = b"screwtapello"
        f[xlfd.FAMILY_NAME] = b"testfont"
        f[xlfd.WEIGHT_NAME] = b"medium"
        f[xlfd.SLANT] = xlfd.SLANT_ROMAN
        f[xlfd.SETWIDTH_NAME] = b"normal"
        f[xlfd.ADD_STYLE_NAME] = b""
        f[xlfd.PIXEL_SIZE] = 5
        f[xlfd.POINT_SIZE] = 50
        f[xlfd.RESOLUTION_X] = 75
        f[xlfd.RESOLUTION_Y] = 75
        f[xlfd.SPACING] = xlfd.SPACING_MONOSPACED
        f[xlfd.AVERAGE_WIDTH] = 45
        f[xlfd.CHARSET_REGISTRY] = b"iso10646"
        f[xlfd.CHARSET_ENCODING] = b"1"

        self.assertEqual(xlfd.validate(f), [])

    def test_accept_case_insensitive_values(self):
        """
        xlfd.validate() accepts values with different case than expected.
        """
        f = model.Font(name=FONTNAME.upper(), ptSize=5, xdpi=75, ydpi=75)

        f[xlfd.FOUNDRY] = b"Screwtapello"
        f[xlfd.FAMILY_NAME] = b"TestFont"
        f[xlfd.WEIGHT_NAME] = b"Medium"
        f[xlfd.SLANT] = b"R"
        f[xlfd.SETWIDTH_NAME] = b"Normal"
        f[xlfd.ADD_STYLE_NAME] = b""
        f[xlfd.PIXEL_SIZE] = 5
        f[xlfd.POINT_SIZE] = 50
        f[xlfd.RESOLUTION_X] = 75
        f[xlfd.RESOLUTION_Y] = 75
        f[xlfd.SPACING] = b"M"
        f[xlfd.AVERAGE_WIDTH] = 45
        f[xlfd.CHARSET_REGISTRY] = b"ISO10646"
        f[xlfd.CHARSET_ENCODING] = b"1"

        self.assertEqual(xlfd.validate(f), [])

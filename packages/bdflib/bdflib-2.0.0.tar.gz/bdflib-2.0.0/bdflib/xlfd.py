# bdflib, a library for working with BDF font files
# Copyright (C) 2009-2022, Timothy Allen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Check fonts against the X Logical Font Descriptor conventions.

Fonts in the BDF format can be used for all kinds of things,
but commonly they are used with the traditional X11 font APIs,
built around X Logical Font Descriptors,
which require certain custom properties be set.

To check a BDF font against the XLFD conventions,
use :func:`.validate()`,
which returns a (hopefully empty) list of problems,
represented as subclasses of :class:`.ValidationError`.

If the font is missing properties that can be automatically calculated,
:func:`fix()` will update the font as required.

For more information about these issues,
see the official `X Logical Font Description Conventions`_ specification.

.. _X Logical Font Description Conventions: https://www.x.org/releases/X11R7.6/doc/xorg-docs/specs/XLFD/xlfd.html#fontname_field_definitions

Helpful constants
-----------------

Names for XLFD properties:

.. py:data:: FOUNDRY

    The organisation responsible for making the font,
    a namespace for :data:`FAMILY_NAME`

.. py:data:: FAMILY_NAME

    The human-readable name of the font,
    like "Times New" or "Helvetica"

.. py:data:: WEIGHT_NAME

    The human-readable name of the font's weight,
    like "Bold" or "Thin"

.. py:data:: SLANT

    A code describing the slant style of the font,
    one of the values in :data:`SLANT_VALUES`

.. py:data:: SETWIDTH_NAME

    The human-reaadable name of the font's width,
    like "Expanded" or "Ultracondensed"

.. py:data:: ADD_STYLE_NAME

    A human-readable name that further distinguishes this font
    from other similar fonts; an "additional style" if you will,
    like "Sans Serif" or "Outline"

.. py:data:: PIXEL_SIZE

    The vertical space required for a line of type,
    in pixels,
    usually (but not always)
    the sum of :data:`FONT_ASCENT` and :data:`FONT_DESCENT`

.. py:data:: POINT_SIZE

    The vertical space required for a line of type,
    in deci-points

.. py:data:: RESOLUTION_X

    The horizontal output resolution this font is intended for,
    in dots-per-inch

.. py:data:: RESOLUTION_Y

    The horizontal output resolution this font is intended for,
    in dots-per-inch

.. py:data:: SPACING

    A code describing the spacing of this font,
    one of the values in :data:`SPACING_VALUES` below

.. py:data:: AVERAGE_WIDTH

    The average width of all the characters in this font,
    in deci-pixels.

.. py:data:: CHARSET_REGISTRY

    The organisation responsible for defining
    the character set encoding used by this font,
    a namespace for :data:`CHARSET_ENCODING`

.. py:data:: CHARSET_ENCODING

    The identifier for the character set encoding used by this font

.. py:data:: FONT_ASCENT

    The maxium height above the baseline
    that any glyph in this font touches,
    in pixels

.. py:data:: FONT_DESCENT

    The maxium depth below the baseline
    that any glyph in this font touches,
    in pixels

.. py:data:: DEFAULT_CHAR

    If the software using this font wants to draw a glyph
    that the font does not contain,
    the glyph with this encoding will be drawn instead

Values for the :data:`SLANT` property:

.. py:data:: SLANT_ROMAN

    This font is drawn with upright strokes

.. py:data:: SLANT_ITALIC

    This font is drawn leaning forward,
    often with curves or flourishes

.. py:data:: SLANT_OBLIQUE

    This font is the Roman variant,
    tilted forward

.. py:data:: SLANT_REVERSE_ITALIC

    This font is drawn leaning backward,
    often with curves or flourishes

.. py:data:: SLANT_REVERSE_OBLIQUE

    This font is the Roman variant,
    tilted backward

.. py:data:: SLANT_OTHER

    This font has a tilt that's not any of the above

.. py:data:: SLANT_VALUES

    The :class:`set` of valid :data:`SLANT` values:

Values for the :data:`SPACING` property:

.. py:data:: SPACING_PROPORTIONAL

    Each glyph in this font takes space
    proportional to its natural width,
    so a character like "i" is narrow
    while "m" is wide

.. py:data:: SPACING_MONOSPACED

    Each glyph in this font takes exactly the same space,
    regardless of its natural width

.. py:data:: SPACING_CHARCELL

    Like :data:`SPACING_MONOSPACED`,
    but in addition,
    no part of any glyph sticks out of the space allocated to it

.. py:data:: SPACING_VALUES

    The :class:`set` of valid :data:`SPACING` values:

Classes and functions
---------------------
"""
from math import inf, ceil
import typing

from bdflib import model

FOUNDRY = b"FOUNDRY"
FAMILY_NAME = b"FAMILY_NAME"
WEIGHT_NAME = b"WEIGHT_NAME"
SLANT = b"SLANT"
SETWIDTH_NAME = b"SETWIDTH_NAME"
ADD_STYLE_NAME = b"ADD_STYLE_NAME"
PIXEL_SIZE = b"PIXEL_SIZE"
POINT_SIZE = b"POINT_SIZE"
RESOLUTION_X = b"RESOLUTION_X"
RESOLUTION_Y = b"RESOLUTION_Y"
SPACING = b"SPACING"
AVERAGE_WIDTH = b"AVERAGE_WIDTH"
CHARSET_REGISTRY = b"CHARSET_REGISTRY"
CHARSET_ENCODING = b"CHARSET_ENCODING"
FONT_ASCENT = b"FONT_ASCENT"
FONT_DESCENT = b"FONT_DESCENT"
DEFAULT_CHAR = b"DEFAULT_CHAR"

SLANT_ROMAN = b"r"
SLANT_ITALIC = b"i"
SLANT_OBLIQUE = b"o"
SLANT_REVERSE_ITALIC = b"ri"
SLANT_REVERSE_OBLIQUE = b"ro"
SLANT_OTHER = b"ot"

SLANT_VALUES = {
    SLANT_ROMAN,
    SLANT_ITALIC,
    SLANT_OBLIQUE,
    SLANT_REVERSE_ITALIC,
    SLANT_REVERSE_OBLIQUE,
    SLANT_OTHER,
}

SPACING_PROPORTIONAL = b"p"
SPACING_MONOSPACED = b"m"
SPACING_CHARCELL = b"c"

SPACING_VALUES = {SPACING_PROPORTIONAL, SPACING_MONOSPACED, SPACING_CHARCELL}


class ValidationError(ValueError):
    """
    Superclass of all problems detected by :func:`.validate()`
    """

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ValidationError):
            return self.args == other.args
        else:
            return False


class NotAnXlfd(ValidationError):
    """
    The font's name is not a valid XLFD string
    """

    pass


class MissingProperty(ValidationError):
    """
    The font is missing a property required by the XLFD conventions
    """

    pass


class Contradiction(ValidationError):
    """
    A value in the XLFD name contradicts a BDF property value
    """

    #: The property name with conflicting values
    name: bytes

    #: The value associated with the BDF property
    prop_value: model.PropertyValue

    #: The value stored in the XLFD name
    xlfd_value: model.PropertyValue

    def __init__(
        self,
        name: bytes,
        prop_value: model.PropertyValue,
        xlfd_value: model.PropertyValue,
    ) -> None:
        super().__init__(name, prop_value, xlfd_value)

        self.name = name
        self.prop_value = prop_value
        self.xlfd_value = xlfd_value

    def __str__(self) -> str:
        return (
            "{name!r} value {prop!r} conflicts with XLFD value {xlfd!r}".format(
                name=self.name,
                prop=self.prop_value,
                xlfd=self.xlfd_value,
            )
        )


class ExpectedInteger(ValidationError):
    """
    The value of a property should be an integer
    """

    #: The name of the property whose value should be an integer
    name: bytes

    #: The value that is not an integer
    value: bytes

    def __init__(self, name: bytes, value: bytes) -> None:
        super().__init__(name, value)

        self.name = name
        self.value = value

    def __str__(self) -> str:
        return "{name!r} value should be bytestring, not {value!r}".format(
            name=self.name, value=self.value
        )


class ExpectedBytestring(ValidationError):
    """
    The value of a property should be a bytestring
    """

    #: The name of the property whose value should be a bytestring
    name: bytes

    #: The value that is not a bytestring
    value: int

    def __init__(self, name: bytes, value: int) -> None:
        super().__init__(name, value)

        self.name = name
        self.value = value

    def __str__(self) -> str:
        return "{name!r} value should be integer, not {value!r}".format(
            name=self.name, value=self.value
        )


class ExpectedEnumeratedValue(ValidationError):
    """
    The value of a property should be one of a fixed set of values
    """

    #: The name of the property with an invalid value
    name: bytes

    #: The value that is not in the expected set
    value: model.PropertyValue

    #: The set of possible values
    expected: typing.Set[bytes]

    def __init__(
        self,
        name: bytes,
        value: model.PropertyValue,
        expected: typing.Set[bytes],
    ) -> None:
        super().__init__(name, value, expected)

        self.name = name
        self.value = value
        self.expected = expected

    def __str__(self) -> str:
        return "{name!r} value should be one of {expected!r}, not {value!r}".format(
            name=self.name, value=self.value, expected=self.expected
        )


def _calculate_properties(
    font: model.Font,
) -> model.Properties:
    res: model.Properties = {}

    # XLFD stores point sizes in tenths of a point.
    res[POINT_SIZE] = font.ptSize * 10

    # Measure the font metrics ourselves.
    minAdvance = inf
    maxAdvance = 0
    totalAdvance = 0
    glyphOverflowsBounds = False
    maxAscent = 0
    maxDescent = 0
    count = 0

    for glyph in font.glyphs:
        minAdvance = min(minAdvance, glyph.advance)
        maxAdvance = max(maxAdvance, glyph.advance)
        totalAdvance += glyph.advance

        if glyph.bbX < 0 or glyph.bbX + glyph.bbW > glyph.advance:
            glyphOverflowsBounds = True

        maxAscent = max(maxAscent, glyph.bbY + glyph.bbH)
        maxDescent = max(maxDescent, -1 * glyph.bbY)
        count += 1

    res[AVERAGE_WIDTH] = int(10 * totalAdvance / count)

    res[FONT_ASCENT] = maxAscent
    res[FONT_DESCENT] = maxDescent

    if minAdvance == maxAdvance:
        if glyphOverflowsBounds:
            res[SPACING] = SPACING_MONOSPACED
        else:
            res[SPACING] = SPACING_CHARCELL
    else:
        res[SPACING] = SPACING_PROPORTIONAL

    if font.glyphs_by_codepoint:
        res[DEFAULT_CHAR] = max(font.glyphs_by_codepoint.keys())

    return res


def _parse_xlfd(
    xlfd: bytes, errors: typing.List[ValidationError]
) -> model.Properties:
    res: model.Properties = {}

    for bad_char in (b"?", b"*", b",", b'"'):
        # XLFD Conventions, Chapter 3
        # An XLFD cannot contain:
        #
        # - the font name wildcard characters * or ?
        # - the font-name separator, ","
        # - the font-name quoting character '"'
        #
        # It also cannot contain a "-" other than as a delimeter,
        # but we'll catch that below.
        if bad_char in xlfd:
            errors.append(NotAnXlfd(xlfd))
            return res

    parts = xlfd.split(b"-")
    if parts[0] != b"":
        # XLFD Conventions, Chapter 8
        # requires that "The FontName begins with
        # the X FontNameRegistry prefix: '-'."
        # (i.e. it follows the standard structure, not the private structure.
        errors.append(NotAnXlfd(xlfd))
        return res

    if len(parts) != 15:
        # XLFD Conventions, Chapter 3
        # After the initial "-" are 14 "-" separated fields.
        errors.append(NotAnXlfd(xlfd))
        return res

    res[FOUNDRY] = parts[1]
    res[FAMILY_NAME] = parts[2]
    res[WEIGHT_NAME] = parts[3]

    if parts[4].lower() in SLANT_VALUES:
        res[SLANT] = parts[4]
    else:
        errors.append(ExpectedEnumeratedValue(SLANT, parts[4], SLANT_VALUES))

    res[SETWIDTH_NAME] = parts[5]
    res[ADD_STYLE_NAME] = parts[6]

    try:
        res[PIXEL_SIZE] = int(parts[7])
    except ValueError:
        errors.append(ExpectedInteger(PIXEL_SIZE, parts[7]))

    try:
        res[POINT_SIZE] = int(parts[8])
    except ValueError:
        errors.append(ExpectedInteger(POINT_SIZE, parts[8]))

    try:
        res[RESOLUTION_X] = int(parts[9])
    except ValueError:
        errors.append(ExpectedInteger(RESOLUTION_X, parts[9]))

    try:
        res[RESOLUTION_Y] = int(parts[10])
    except ValueError:
        errors.append(ExpectedInteger(RESOLUTION_Y, parts[10]))

    if parts[11].lower() in SPACING_VALUES:
        res[SPACING] = parts[11]
    else:
        errors.append(
            ExpectedEnumeratedValue(SPACING, parts[11], SPACING_VALUES)
        )

    try:
        res[AVERAGE_WIDTH] = int(parts[12])
    except ValueError:
        errors.append(ExpectedInteger(AVERAGE_WIDTH, parts[12]))

    res[CHARSET_REGISTRY] = parts[13]
    res[CHARSET_ENCODING] = parts[14]

    return res


def fix(font: model.Font) -> None:
    """
    Add missing XLFD properties to a font, with default or calculated values

    Any properties already present will be preserved,
    even if their values seem to be incorrect.
    """

    # The default values for every font.
    properties: model.Properties = {
        POINT_SIZE: font.ptSize,
        PIXEL_SIZE: ceil(font.ydpi * font.ptSize / 72.0),
        RESOLUTION_X: font.xdpi,
        RESOLUTION_Y: font.ydpi,
        WEIGHT_NAME: b"Medium",
        SLANT: SLANT_ROMAN,
        SETWIDTH_NAME: b"Normal",
        ADD_STYLE_NAME: b"",
    }

    # Add the properties we can calculate from font data.
    properties.update(_calculate_properties(font))

    # Add our new properties to the font,
    # but don't overwrite any existing properties.
    properties.update(font.properties)
    font.properties = properties


def _check_missing(
    font: model.Font, errors: typing.List[ValidationError], key: bytes
) -> None:
    if key not in font.properties:
        errors.append(MissingProperty(key))
        return


def _check_value(
    font: model.Font,
    errors: typing.List[ValidationError],
    key: bytes,
    expected_type: type,
    expected_values: typing.Optional[typing.Set[bytes]] = None,
) -> None:
    if key not in font.properties:
        # We check for missing properties in _check_missing
        return

    value = font[key]

    if not isinstance(value, expected_type):
        if expected_type == bytes:
            errors.append(ExpectedBytestring(key, value))
        else:
            errors.append(ExpectedInteger(key, value))

    # XLFD strings are case-insensitive.
    if isinstance(value, bytes):
        normalised_value = value.lower()
    else:
        normalised_value = value

    if expected_values is not None and normalised_value not in expected_values:
        errors.append(ExpectedEnumeratedValue(key, value, expected_values))


def _compare_property(
    bdf_properties: model.Properties,
    xlfd_properties: model.Properties,
    errors: typing.List[ValidationError],
    key: bytes,
) -> None:
    if key not in bdf_properties or key not in xlfd_properties:
        # We validate missing properties in _check_missing.
        return

    bdf_value = bdf_properties[key]
    xlfd_value = xlfd_properties[key]

    normalised_bdf_value: model.PropertyValue
    normalised_xlfd_value: model.PropertyValue

    # XLFD strings are case-insensitive.
    if isinstance(bdf_value, bytes):
        normalised_bdf_value = bdf_value.lower()
    else:
        normalised_bdf_value = bdf_value

    if isinstance(xlfd_value, bytes):
        normalised_xlfd_value = xlfd_value.lower()
    else:
        normalised_xlfd_value = xlfd_value

    if normalised_bdf_value != normalised_xlfd_value:
        errors.append(Contradiction(key, bdf_value, xlfd_value))


def validate(font: model.Font) -> typing.List[ValidationError]:
    """
    Validate a font against the XLFD conventions

    This function checks for missing, required properties,
    properties with the wrong type,
    the syntax of the font's XLFD name
    and conflicts between the XLFD name and its properties.

    All problems detected
    (not just the first)
    are returned in a list.
    """
    res: typing.List[ValidationError] = []

    # XLFD Conventions, chapter 8:
    # the 14 values included in the XLFD
    # must also be present as properties.
    _check_missing(font, res, FOUNDRY)
    _check_missing(font, res, FAMILY_NAME)
    _check_missing(font, res, WEIGHT_NAME)
    _check_missing(font, res, SLANT)
    _check_missing(font, res, SETWIDTH_NAME)
    _check_missing(font, res, ADD_STYLE_NAME)
    _check_missing(font, res, PIXEL_SIZE)
    _check_missing(font, res, POINT_SIZE)
    _check_missing(font, res, RESOLUTION_X)
    _check_missing(font, res, RESOLUTION_Y)
    _check_missing(font, res, SPACING)
    _check_missing(font, res, AVERAGE_WIDTH)
    _check_missing(font, res, CHARSET_REGISTRY)
    _check_missing(font, res, CHARSET_ENCODING)

    # XLFD Conventions, chapter 8:
    # "Any FontProperties provided
    # conform in name and semantics
    # to the XLFD FontProperty definitions."
    _check_value(font, res, FOUNDRY, bytes)
    _check_value(font, res, FAMILY_NAME, bytes)
    _check_value(font, res, WEIGHT_NAME, bytes)
    _check_value(font, res, SLANT, bytes, SLANT_VALUES)
    _check_value(font, res, SETWIDTH_NAME, bytes)
    _check_value(font, res, ADD_STYLE_NAME, bytes)
    _check_value(font, res, PIXEL_SIZE, int)
    _check_value(font, res, POINT_SIZE, int)
    _check_value(font, res, RESOLUTION_X, int)
    _check_value(font, res, RESOLUTION_Y, int)
    _check_value(font, res, SPACING, bytes, SPACING_VALUES)
    _check_value(font, res, AVERAGE_WIDTH, int)
    _check_value(font, res, CHARSET_REGISTRY, bytes)
    _check_value(font, res, CHARSET_ENCODING, bytes)
    _check_value(font, res, b"MIN_SPACE", int)
    _check_value(font, res, b"NORM_SPACE", int)
    _check_value(font, res, b"MAX_SPACE", int)
    _check_value(font, res, b"END_SPACE", int)
    _check_value(font, res, b"AVG_CAPITAL_WIDTH", int)
    _check_value(font, res, b"AVG_LOWERCASE_WIDTH", int)
    _check_value(font, res, b"QUAD_WIDTH", int)
    _check_value(font, res, b"FIGURE_WIDTH", int)
    _check_value(font, res, b"SUPERSCRIPT_X", int)
    _check_value(font, res, b"SUPERSCRIPT_Y", int)
    _check_value(font, res, b"SUBSCRIPT_X", int)
    _check_value(font, res, b"SUBSCRIPT_Y", int)
    _check_value(font, res, b"SUPERSCRIPT_SIZE", int)
    _check_value(font, res, b"SUBSCRIPT_SIZE", int)
    _check_value(font, res, b"SMALL_CAP_SIZE", int)
    _check_value(font, res, b"UNDERLINE_POSITION", int)
    _check_value(font, res, b"UNDERLINE_THICKNESS", int)
    _check_value(font, res, b"STRIKEOUT_ASCENT", int)
    _check_value(font, res, b"STRIKEOUT_DESCENT", int)
    _check_value(font, res, b"ITALIC_ANGLE", int)
    _check_value(font, res, b"CAP_HEIGHT", int)
    _check_value(font, res, b"X_HEIGHT", int)
    _check_value(font, res, b"RELATIVE_SETWIDTH", int)
    _check_value(font, res, b"RELATIVE_WEIGHT", int)
    _check_value(font, res, b"WEIGHT", int)
    _check_value(font, res, b"FACE_NAME", bytes)
    _check_value(font, res, b"COPYRIGHT", bytes)
    _check_value(font, res, b"NOTICE", bytes)
    _check_value(font, res, b"DESTINATION", int)
    _check_value(
        font,
        res,
        b"FONT_TYPE",
        bytes,
        {b"Bitmap", b"Prebuilt", b"Type 1", b"TrueType", b"Speedo", b"F3"},
    )
    _check_value(font, res, b"FONT_VERSION", bytes)
    _check_value(font, res, b"RASTERIZER_NAME", bytes)
    _check_value(font, res, b"RASTERIZER_VERSION", bytes)
    _check_value(font, res, b"RAW_ASCENT", int)
    _check_value(font, res, b"RAW_DESCENT", int)
    _check_value(font, res, FONT_ASCENT, int)
    _check_value(font, res, FONT_DESCENT, int)
    _check_value(
        font, res, DEFAULT_CHAR, int, set(font.glyphs_by_codepoint.keys())
    )

    xlfd_properties = _parse_xlfd(font.name, res)

    # Any fields in the XLFD name that also appear as BDF properties
    # should have values that match the corresponding BDF property value.
    _compare_property(font.properties, xlfd_properties, res, FOUNDRY)
    _compare_property(font.properties, xlfd_properties, res, FAMILY_NAME)
    _compare_property(font.properties, xlfd_properties, res, WEIGHT_NAME)
    _compare_property(font.properties, xlfd_properties, res, SLANT)
    _compare_property(font.properties, xlfd_properties, res, SETWIDTH_NAME)
    _compare_property(font.properties, xlfd_properties, res, ADD_STYLE_NAME)
    _compare_property(font.properties, xlfd_properties, res, PIXEL_SIZE)
    _compare_property(font.properties, xlfd_properties, res, POINT_SIZE)
    _compare_property(font.properties, xlfd_properties, res, RESOLUTION_X)
    _compare_property(font.properties, xlfd_properties, res, RESOLUTION_Y)
    _compare_property(font.properties, xlfd_properties, res, SPACING)
    _compare_property(font.properties, xlfd_properties, res, AVERAGE_WIDTH)
    _compare_property(font.properties, xlfd_properties, res, CHARSET_REGISTRY)
    _compare_property(font.properties, xlfd_properties, res, CHARSET_ENCODING)
    _compare_property(font.properties, xlfd_properties, res, FONT_ASCENT)
    _compare_property(font.properties, xlfd_properties, res, FONT_DESCENT)

    return res

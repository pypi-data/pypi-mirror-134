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

import math


def _quote_property_value(val):
    if isinstance(val, int):
        return b"%d" % val
    else:
        return b'"' + bytes(val).replace(b'"', b'""') + b'"'


def write_bdf(font, stream):
    """
    Write a BDF-format font to the given stream.

    :param Font font: The font to write to the given stream.
    :param stream: The stream that will receive the font.

    ``stream`` must be an object with at ``.write()`` method that takes a
    :class:`bytes`. If you want to write to an actual file, make sure you
    use the 'b' flag::

            bdflib.writer.write_bdf(font, open(path, 'wb'))
    """
    # The font bounding box is the union of glyph bounding boxes.
    font_bbX = 0
    font_bbY = 0
    font_bbW = 0
    font_bbH = 0
    for g in font.glyphs:
        new_bbX = min(font_bbX, g.bbX)
        new_bbY = min(font_bbY, g.bbY)
        new_bbW = max(font_bbX + font_bbW, g.bbX + g.bbW) - new_bbX
        new_bbH = max(font_bbY + font_bbH, g.bbY + g.bbH) - new_bbY

        (font_bbX, font_bbY, font_bbW, font_bbH) = (
            new_bbX,
            new_bbY,
            new_bbW,
            new_bbH,
        )

    font_pixel_size = math.ceil(font.ydpi * font.ptSize / 72.0)

    # Write the basic header.
    stream.write(b"STARTFONT 2.1\n")
    stream.write(b"FONT ")
    stream.write(font.name)
    stream.write(b"\n")
    stream.write(b"SIZE %g %d %d\n" % (font.ptSize, font.xdpi, font.ydpi))
    stream.write(
        b"FONTBOUNDINGBOX %d %d %d %d\n"
        % (font_bbW, font_bbH, font_bbX, font_bbY)
    )

    # Write the properties
    stream.write(b"STARTPROPERTIES %d\n" % (len(font.properties),))
    keys = sorted(font.properties.keys())
    for key in keys:
        stream.write(key)
        stream.write(b" ")
        stream.write(_quote_property_value(font.properties[key]))
        stream.write(b"\n")
    stream.write(b"ENDPROPERTIES\n")

    # Write out the glyphs
    stream.write(b"CHARS %d\n" % (len(font.glyphs),))
    for glyph in font.glyphs:
        scalable_width = int(1000.0 * glyph.advance / font_pixel_size)
        stream.write(b"STARTCHAR ")
        stream.write(glyph.name)
        stream.write(b"\n")
        stream.write(b"ENCODING %d\n" % (glyph.codepoint,))
        stream.write(b"SWIDTH %d 0\n" % (scalable_width,))
        stream.write(b"DWIDTH %d 0\n" % (glyph.advance,))
        stream.write(
            b"BBX %d %d %d %d\n" % (glyph.bbW, glyph.bbH, glyph.bbX, glyph.bbY)
        )
        stream.write(b"BITMAP\n")

        # How many bytes do we need to represent the bits in each row?
        rowWidth, extraBits = divmod(glyph.bbW, 8)

        # How many bits of padding do we need to round up to a full byte?
        if extraBits > 0:
            rowWidth += 1
            paddingBits = 8 - extraBits
        else:
            paddingBits = 0

        # glyph.data goes bottom-to-top
        # like any proper coordinate system does,
        # but rows wants to be top-to-bottom
        # like any proper stream-output.
        for row in reversed(glyph.data):
            # rowWidth is the number of bytes,
            # but Python wants the number of nybbles,
            # so multiply by 2.
            stream.write(b"%0*X\n" % (rowWidth * 2, row << paddingBits))

        stream.write(b"ENDCHAR\n")

    stream.write(b"ENDFONT\n")

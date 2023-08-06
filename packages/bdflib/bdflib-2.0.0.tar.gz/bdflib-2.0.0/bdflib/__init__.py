"""
Read, manipulate and write bitmap fonts in the Bitmap Distribution Format.

To get started, use :func:`bdflib.reader.read_bdf` to load a BDF file and
create a :class:`bdflib.model.Font` object, or just create one yourself from
scratch.

Modify the font by tinkering with it directly, or by using the helpers in
:mod:`bdflib.effects` and :mod:`bdflib.glyph_combining`.
If you're making a font intended for use with the X11 windowing system,
check out the helpers in :mod:`bdflib.xlfd`.

When you're done, you can use :func:`bdflib.writer.write_bdf` to write your
font back out to a BDF file.
"""

__version__ = "2.0.0"

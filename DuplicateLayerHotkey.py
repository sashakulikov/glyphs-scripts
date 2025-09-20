# MenuTitle: Duplicate Current Layer
# Shortcut: Cmd+Alt+C
# -*- coding: utf-8 -*-
__doc__="""
Duplicates the currently selected layer with a timestamped name.
"""

import GlyphsApp
from datetime import datetime

font = Glyphs.font
layer = font.selectedLayers[0]
glyph = layer.parent

# Duplicate current layer
duplicate = layer.copy()

# Timestamp
timestamp = datetime.now().strftime("%d. %b %y at %H:%M")
duplicate.name = timestamp

# Insert new layer
glyph.layers.append(duplicate)

# Select the new layer
font.selectedLayers[0] = duplicate

print(f"Duplicated layer in glyph: {glyph.name} → {duplicate.name}")
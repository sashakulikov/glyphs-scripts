#MenuTitle: Show Glyphs with Component
# -*- coding: utf-8 -*-
__doc__="""
Opens a new tab with all glyphs that contain a specified component.
"""

import GlyphsApp
import vanilla

class FindComponentDialog(object):
    def __init__(self):
        # Window
        self.w = vanilla.FloatingWindow((320, 70), "Find Component")

        # UI elements
        self.w.text = vanilla.TextBox((10, 12, 80, 20), "Component:")
        self.w.input = vanilla.EditText((90, 10, -90, 22), "")
        self.w.button = vanilla.Button((-70, 10, -10, 22), "OK", callback=self.runScript)

        # Make Enter key trigger OK
        self.w.setDefaultButton(self.w.button)

        # Show window
        self.w.open()
        self.w.makeKey()

    def runScript(self, sender):
        # Get component name
        targetComponent = self.w.input.get().strip()
        if not targetComponent:
            GlyphsApp.Message("No component entered", "Please type a component name.")
            return

        # Search for component in font
        font = Glyphs.font
        found = []

        for g in font.glyphs:
            for layer in g.layers:
                for comp in layer.components:
                    if comp.componentName == targetComponent:
                        found.append("/" + g.name)
                        break  # Stop after first match in this glyph

        # Open results in new tab
        if found:
            font.newTab(" ".join(found))
        else:
            GlyphsApp.Message("No matches", f"No glyphs contain '{targetComponent}'.", OKButton=None)

        # Close window
        self.w.close()

# Run script
FindComponentDialog()
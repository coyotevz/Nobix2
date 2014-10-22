"""
    nobix.ui.window
    ~~~~~~~~~~~~~~~
"""

import urwid
from urwid import Frame, Filler, Text, AttrMap

class MainWindow(Frame):

    def __init__(self, app):
        self.app = app
        self.__super.__init__(
            Filler(Text("<Docuemnt Body>")),
            Text("<Document Header>"),
            Text("<Document Footer>"),
        )

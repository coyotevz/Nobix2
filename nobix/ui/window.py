"""
    nobix.ui.window
    ~~~~~~~~~~~~~~~
"""

import urwid
from urwid import Frame, Filler, Text, AttrMap

class MainWindow(Frame):

    def __init__(self, app):
        self.app = app
        self.build_widgets()

        self.__super.__init__(
            Filler(Text("<Main Body>")),
            self.menubar,
            self.statusbar,
        )

    def build_widgets(self):
        self.menubar = AttrMap(Text("<Menu Bar>"), 'menubar')
        self.statusbar = AttrMap(Text("<Status Bar>"), 'statusbar')

    def toggle_statusbar(self):
        if 'footer' in self.contents.keys():
            del self.contents['footer']
        else:
            self.contents['footer'] = (self.statusbar, None)

    def toggle_menubar(self):
        if 'header' in self.contents.keys():
            del self.contents['header']
        else:
            self.contents['header'] = (self.menubar, None)

    def keypress(self, size, key):
        if key == 'f9':
            self.toggle_menubar()
        elif key == 'f8':
            self.toggle_statusbar()

        return super(MainWindow, self).keypress(size, key)

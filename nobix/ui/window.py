"""
    nobix.ui.window
    ~~~~~~~~~~~~~~~
"""

import urwid
from urwid import Frame, Filler, Text, AttrMap


class MenuBar(urwid.WidgetWrap):

    def __init__(self, menus=None):
        self.menus = menus or []
        columns = self._build()
        super(MenuBar, self).__init__(columns)

    def _build(self):
        return AttrMap(urwid.Columns([('pack', urwid.Text(' '+t+' ')) for t in self.menus],
                                     dividechars=3), 'menubar')

    def add_menu(self, menu):
        self.menus.append(menu)
        self._w = self._build()

class MainWindow(Frame):

    def __init__(self, app):
        self.app = app
        self.build_widgets()

        self.__super.__init__(
            AttrMap(Filler(Text("<Main Body>")), 'mainbody'),
            self.menubar,
            self.statusbar,
        )

    def build_widgets(self):
        #self.menubar = AttrMap(Text("<Menu Bar>"), 'menubar')
        self.menubar = MenuBar(['a', 'ab'])
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
        elif key == 'f7':
            self.menubar.add_menu('f7')

        return super(MainWindow, self).keypress(size, key)

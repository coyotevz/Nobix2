"""
    nobix.mainloop
    ~~~~~~~~~~~~~~
"""

import urwid

class MainLoop(urwid.MainLoop):

    def quit(self):
        """Stop loop"""
        raise urwid.ExitMainLoop()

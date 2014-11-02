"""
    nobix.app
    ~~~~~~~~~

    Main application module.
"""

import sys
from configparser import ConfigParser

from nobix.mainloop import MainLoop
from nobix.ui import MainWindow

class Application(object):

    allowed_colors = (1, 16, 88, 256)

    def __init__(self, appname='nobix'):
        self.appname = appname
        self.conf = ConfigParser()

    def run(self, args=None):
        """Main entry point for application"""
        if args is None:
            args = sys.argv[1:]

        self.configure()
        self.init_ui()
        self.main_loop()

    def configure(self):
        self.conf.read('nobix.cfg')

    def init_ui(self):
        colors = self.conf.getint("ui", "colors")
        skins_dir = self.conf.get("paths", "skins")

        if colors not in self.allowed_colors:
            self.stop()

        self.window = MainWindow(self)

    def main_loop(self):
        tmp_palette = [
            ('menubar', 'dark gray', 'light gray'),
            ('statusbar', 'white', 'dark cyan'),
        ]
        self.loop = MainLoop(self.window,
                             palette=tmp_palette,
                             unhandled_input=self.unhandled_input)
        self.loop.run()

    def quit(self):
        self.loop.quit()

    def unhandled_input(self, key):
        if key in ('q', 'Q'):
            self.quit()


def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    main()

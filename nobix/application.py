"""
    nobix.application
    ~~~~~~~~~~~~~~~~~

    Main application module.
"""

import sys

from nobix.mainloop import MainLoop
from nobix.ui import MainWindow

class Application(object):

    def __init__(self, appname='nobix'):
        self.appname = appname

    def run(self, args=None):
        """Main entry point for application"""
        if args is None:
            args = sys.argv[1:]

        if len(args) == 0:
            return self.run_nobix()
        elif args[0] == "create_password":
            return self.run_create_password()
        elif args[0] == "shell":
            return self.run_shell()
        elif args[0] in ("usage", "-h", "--help"):
            self.run_usage()
        else:
            print("args:", args)
            print("ERROR: Argumentos incorrectos")
            self.run_usage()

    def run_usage(self):
        sys.exit("Uso: {} [comando]\n"
        "\n"
        "Si [comando] no se especifica se lanza el programa normalmente.\n"
        "\n"
        "[comando] puede ser uno de los siguientes:\n"
        "\n"
        "create_password  -- Genera la contraseña md5 para un usuario.\n"
        "shell            -- Abre una consola con algunos modulos pre-cargados.\n"
        "usage,-h,--help  -- Muestra este mensaje de ayuda.\n"
        "\n"
        "--database-uri   -- URI de la base de datos como la recibe SQLAlchemy."
        "".format(self.appname))

    def run_nobix(self):
        self.create_ui()
        self._run()

    def run_create_password(self):
        print("Run create_password")

    def run_shell(self):
        print("Run shell")

    def create_ui(self):
        self.main_window = MainWindow(self)

    def _run(self):
        self.loop = MainLoop(self.main_window,
                             unhandled_input=self.unhandled_input)
        self.loop.run()

    def stop(self):
        self.loop.quit()

    def unhandled_input(self, key):
        if key in ('q', 'Q'):
            self.stop()


def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    main()

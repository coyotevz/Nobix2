from setuptools import setup, find_packages

NAME = "Nobix"
VERSION = "0.1.0"


setup(
    name = NAME,
    version = VERSION,
    url = "http://github.com/coyotevz/Nobix",
    author = "Augusto Roccasalva",
    author_email = "augusto@rioplomo.com.ar",
    license = "GPLv3",
    packages = find_packages(),

    entry_points = {
        'console_scripts': [
            'nobix = nobix.application:main',
        ],
    },

    install_requires = [
        'urwid',
        'SQLAlchemy',
        'Mako',
    ],
)

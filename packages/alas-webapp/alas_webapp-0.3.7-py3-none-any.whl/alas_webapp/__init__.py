import os

from .__version__ import __version__


def app_file():
    folder = os.path.dirname(__file__)
    file = os.path.join(folder, './app.asar')
    return os.path.abspath(file)

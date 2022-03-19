import eel
import os


class Sqlsetting:
    def __init__(self) -> None:
        pass

    def addData(self) -> None:
        pass

    def check(self) -> None:
        pass


@eel.expose
def register():
    pass


@eel.expose
def login():
    pass


eel.init(f"{os.path.dirname(os.path.realpath(__file__))}/web")

eel.start("index.html")

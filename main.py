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
def register() -> str:
    return "True"


@eel.expose
def login() -> str:
    return "True"


eel.init(f"{os.path.dirname(os.path.realpath(__file__))}/web")

eel.start("index.html")

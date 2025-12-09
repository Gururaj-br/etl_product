from engine.base import Engine
from config import *

class SqlEngine(Engine):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        print("Running SQL Engine")
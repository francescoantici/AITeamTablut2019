import sys
sys.path.append("/Users/francesco/Documents/Fundamentals/tablut/Tablut2019/lib")
import games4e
import numpy as np

stato=np.zeros((10,9))
class MyGame(games4e.Game):
    "The state in this game would be managed as a numpy 2-D array"
    def __init__(self, state):
        self.initial = state
    


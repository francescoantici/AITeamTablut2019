import sys
sys.path.append("/Users/francesco/Documents/Fundamentals/tablut/Tablut2019/lib")
import games4e
import numpy as np

stato=np.zeros((10,9))
class MyGame(games4e.Game):
    "The state in this game would be managed as a numpy 2-D array"
    def __init__(self,state):
        self.initial=state
    


class State:
    def __init__(self,init_state):
        self.__turn=True #0 is for the white player, 1 for the black player
        self.__playboard=init_state
    def to_move(self):
        if self.__turn == 0:
            self.__turn=1
        else:
            self.__turn=0
        
        return self.__turn


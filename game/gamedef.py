import sys
sys.path.append("/Users/francesco/Documents/Fundamentals/tablut/Tablut2019/lib")
import games4e
import numpy as np

stato=np.zeros((10,9))
class MyGame(games4e.Game):
    "The state in this game would be managed as a numpy 2-D array"
    def __init__(self, state):
        self.initial = state
    def actions(self,state):
        L=[]
        camps=[(0,3),(0,4),(0,5),(1,4),(3,0),(4,0),(5,0),(4,1),(4,7),(3,8),(4,8),(5,8),(7,4),(8,3),(8,4),(8,5)]
        for i in range(state.__playboard.shape[0]):
            for j in range(state.__playboard.shape[1]):
                if state.__playboard[i,j] == 0:
                    continue
                elif state.__playboard[i,j] > 0:

                    
                else:
                    continue #black actions

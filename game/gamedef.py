import sys
sys.path.append("/Users/francesco/Documents/Fundamentals/tablut/Tablut2019/lib")
import games4e
import numpy as np
import State

stato=np.zeros((10,9))
class MyGame(games4e.Game):
    "The state in this game would be managed as a numpy 2-D array"
    def __init__(self, state):
        self.initial = state.playboard
    def actions(self,state):
        L=[]
        for i in range(state.playboard.shape[0]):
            for j in range(state.playboard.shape[1]):
                if state.playboard[i,j] == 0:
                    continue
                elif state.playboard[i,j] > 0:
                    for k in range(state.playboard.shape[0]):
                        #check if the poition is valid by avoiding considering moves into camps, other checkers position and the starting one
                        if (k,j)==(i,j) or (k,j) in state.camps or state.playboard[k,j] != 0: 
                            continue
                        else:
                                L.append((i,j,k,j))
                    for q in range(state.playboard.shape[1]):
                        if (i,q)==(i,j) or (i,q) in state.camps or state.playboard[i,q] != 0: 
                            continue
                        else:
                                L.append((i,j,i,q))
                    
                else:
                    continue #black actions
        return L

p=np.array([[0,0,0,-1,-1,-1,0,0,0],
            [0,0,0,0,-1,0,0,0,0],
            [0,0,0,0,1,0,0,0,0],
            [-1,0,0,0,1,0,0,0,-1],
            [-1,-1,1,1,2,1,1,-1,-1],
            [-1,0,0,0,1,0,0,0,-1],
            [0,0,0,0,1,0,0,0,0],
            [0,0,0,0,-1,0,0,0,0],
            [0,0,0,-1,-1,-1,0,0,0]])
s=State.State(p)
g=MyGame(s)
print(g.actions(s))
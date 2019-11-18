import libs.games4e
import numpy as np
import game.State

stato=np.zeros((10,9))
class MyGame(games4e.Game):
    "The state in this game would be managed as a numpy 2-D array"
    def __init__(self, state):
        self.initial = state.playboard
    def actions(self,state,player):
        L=[]
        if player:
            L=self.bactions(state)
        else:
            L=self.wactions(state)
        
        return L
    def wactions(self,state):
        L=[]
        for i in range(state.playboard.shape[0]):
            for j in range(state.playboard.shape[1]):
                if state.playboard[i,j] == 0:
                    continue  #empty position
                elif state.playboard[i,j] < 0:
                    continue  #black checker
                else:
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
        return L    
    def bactions(self,state):
        L=[]
        for i in range(state.playboard.shape[0]):
            for j in range(state.playboard.shape[1]):
                if state.playboard[i,j] == 0:
                    continue  #empty position
                elif state.playboard[i,j] > 0:
                    continue  #white checker
                else:
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
                    
        return L        
               
    def result(self,state,move):
        a=state.playboard[move[0],move[1]]
        state.playboard[move[0],move[1]]=0
        state.playboard[move[2],move[3]]=a
        return state
    def terminal_test(self,state,player):
        if player:
            if self.KingTrapped(state):
                return True
            else:
                return False
        else:
            if self.KingPosition(state) in state.escapes:
                return True
            else:
                return False

    def KingPosition(self,state):
         for i in range(state.playboard.shape[0]):
            for j in range(state.playboard.shape[1]):
                if state.playboard[i,j]==2:
                    return (i,j)

    def ksurrounded(self,state):  #i don't need the king position, because i call this method only when the king is in the castle
        if state.playboard[4,3] != -1 or state.playboard[4,5] != -1 or state.playboard[3,4] != -1 or state.playboard[5,4] != -1 :
            return False
        else:
            return True

    def surrounded(self,position,state): #control if a checker in position position is surrounded by other checkers 
        vsurrounded=False
        hsurrounded=False
        #horizontal check
        if (state.playboard[position[0],position[1]-1] >= -state.playboard[position[0],position[1]] or (position[0],position[1]-1) in state.camps or (position[0],position[1]-1) in state.castle) and (state.playboard[position[0],position[1]+1] >= -state.playboard[position[0],position[1]] or (position[0],position[1]+1) in state.camps or (position[0],position[1]+1) in state.castle):
            hsurrounded=True
        #vertical check
        if (state.playboard[position[0]-1,position[1]] >= -state.playboard[position[0],position[1]] or (position[0]-1,position[1]) in state.camps or (position[0]-1,position[1]) in state.castle) and (state.playboard[position[0]+1,position[1]] >= -state.playboard[position[0],position[1]] or (position[0]+1,position[1]) in state.camps or (position[0]+1,position[1]) in state.castle):
            vsurrounded=True
        if position == self.KingPosition(state):
            return hsurrounded and vsurrounded
        else:
            return hsurrounded or vsurrounded

    def KingTrapped(self,state):
        KP=self.KingPosition(state)
        if KP in state.castle:
            return self.ksurrounded(state)
        else:
            return self.surrounded(KP,state)
    def display(self,state):
        print(state.playboard)

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





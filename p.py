#Assignment 2 -- 2(8 PUZZLE PROBLEM)
#State Space Representation 
import copy
from queue import PriorityQueue
class puzzle(object):
    def __init__(self,initial,goal):
        self.parent=None
        self.curr=copy.deepcopy(initial)
        self.level=0
        self.empty=self.getemptyindex()
        #for ease
        self.stateno=1
        self.empty1=self.empty[0]
        self.empty2=self.empty[1]
        self.goal=copy.deepcopy(goal)
        #self.h1=self.heuristic1()
        #self.h2=self.heuristic2()
    def getemptyindex(self):
        arr=[]
        for i in range(0,3):
            for j in range(0,3):
                if (self.curr[i][j]==0):
                    arr.append([i,j])
        return (arr)
    def display_state(self):
        # self.stateno+=1
        for i in range(0,3):
            for j in range(0,3):
                print(self.curr[i][j],end="\t")
            print("\n")
        
    def isgoalreached(self):
        for i in range(0,3,1):
            for j in range(0,3):
                if (self.curr[i][j]!=self.goal[i][j]):
                    return False
        return True
    # def displaysolution(self):
    #     print("--------SOLUTION--------")
    #     while self.parent:
    #         print("STATE ",self.stateno)
    #         self.display_state()
    #         self=self.parent
    #     print("STATE ",self.stateno)
    #     self.display_state()
    def displaysolution(self):
        print("--------SOLUTION--------")
        path = []
        while self:
            path.append(self)
            self = self.parent

        for state in reversed(path):
            print("STATE ", state.level)
            state.display_state()            
    #self.empty[0] and self.empty[1]
    #actions
    #if has logic created for rules -- here the up,down,left and right work on the empty spaces
    def lefttilea(self):
        if (self.empty1[1]>=1):
            self.curr[self.empty1[0]][self.empty1[1]],self.curr[self.empty1[0]][self.empty1[1]-1]=self.curr[self.empty1[0]][self.empty1[1]-1],self.curr[self.empty1[0]][self.empty1[1]]
            self.empty1[1]=self.empty1[1]-1
            if(self.isgoalreached()):
                print("Goal is reached")
            return True

        else:
            print("Invalid Move")
            return False
        
    def lefttileb(self):
        if (self.empty2[1]>=1):
            self.curr[self.empty2[0]][self.empty2[1]],self.curr[self.empty2[0]][self.empty2[1]-1]=self.curr[self.empty2[0]][self.empty2[1]-1],self.curr[self.empty2[0]][self.empty2[1]]
            self.empty2[1]=self.empty2[1]-1
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
        else:
            print("Invalid Move")
            return False
        
    def righttilea(self):
        if (self.empty1[1]<=1):
            self.curr[self.empty1[0]][self.empty1[1]],self.curr[self.empty1[0]][self.empty1[1]+1]=self.curr[self.empty1[0]][self.empty1[1]+1],self.curr[self.empty1[0]][self.empty1[1]]
            self.empty1[1]=self.empty1[1]+1            
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            print("Invalid Move")
            return False
        
    def righttileb(self):
        if (self.empty2[1]<=1):
            self.curr[self.empty2[0]][self.empty2[1]],self.curr[self.empty2[0]][self.empty2[1]+1]=self.curr[self.empty2[0]][self.empty2[1]+1],self.curr[self.empty2[0]][self.empty2[1]]
            self.empty2[1]=self.empty2[1]+1            
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            print("Invalid Move")
            return False
        
    def uptilea(self):
        if (self.empty1[0]>=1):
            self.curr[self.empty1[0]][self.empty1[1]],self.curr[self.empty1[0]-1][self.empty1[1]]=self.curr[self.empty1[0]-1][self.empty1[1]],self.curr[self.empty1[0]][self.empty1[1]]
            self.empty1[0]=self.empty1[0]-1            
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            print("Invalid Move")
            return False

    def uptileb(self):
        if (self.empty2[0]>=1):
            self.curr[self.empty2[0]][self.empty2[1]],self.curr[self.empty2[0]-1][self.empty2[1]]=self.curr[self.empty2[0]-1][self.empty2[1]],self.curr[self.empty2[0]][self.empty2[1]]
            self.empty2[0]=self.empty2[0]-1            
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            print("Invalid Move")
            return False
        
        
    def downtilea(self):
        if (self.empty1[0]<=1):
            self.curr[self.empty1[0]][self.empty1[1]],self.curr[self.empty1[0]+1][self.empty1[1]]=self.curr[self.empty1[0]+1][self.empty1[1]],self.curr[self.empty1[0]][self.empty1[1]]
            self.empty1[0]=self.empty1[0]+1            
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            print("Invalid Move")
            return False

    def downtileb(self):
        if (self.empty2[0]<=1):
            self.curr[self.empty2[0]][self.empty2[1]],self.curr[self.empty2[0]+1][self.empty2[1]]=self.curr[self.empty2[0]+1][self.empty2[1]],self.curr[self.empty2[0]][self.empty2[1]]
            self.empty2[0]=self.empty2[0]+1            
            if(self.isgoalreached()):
                print("Goal is reached")
            return True
            
        else:
            print("Invalid Move")   
            return False
    def getxindex(self,value):
        for i in range(0,3):
            for j in range(0,3):
                if self.goal[i][j]==value:
                    return i
    def getyindex(self,value):
        for i in range(0,3):
            for j in range(0,3):
                if self.goal[i][j]==value:
                    return j
    def heuristic1(self):
        count=0
        for i in range(0,3):
            for j in range(0,3):
                if self.curr[i][j]==self.goal[i][j]:
                    count+=1
        return count  
    def heuristic2(self):
        dist=0
        for i in range(0,3):
            for j in range(0,3):
                val=self.curr[i][j]
                dist+=abs(i-self.getxindex(val))+abs((j-self.getyindex(val)))
        return dist
    # def compare(self,p2):
    #     for i in range(3):
    #         for j in range(3):
    #             if self.curr[i][j]!=p2.curr[i][j]:
    #                 return False
    #     return True
    # def sortparameter(self):
    #     return self.level+self.heuristic1()
    def __lt__(self,other):
        return self.level+self.heuristic2()<other.level+other.heuristic2()
        
closed_list=[]
def checkclosed(p1):
    for node in closed_list:
        if node.compare(p1):
            print("INSIDE CLOSED")
            return True
    return False

def astar(p):
    open_stack = PriorityQueue()
    open_stack.put(p)
    closed_set = set()

    while not open_stack.empty():
        current = open_stack.get()
        print("Heuristic 1:", current.heuristic1())
        print("Current State:")
        current.display_state()
        print("Goal State:")
        p.display_state()
        closed_set.add(tuple(map(tuple, current.curr)))  # Store the current state in the closed set

        if current.isgoalreached():
            print("GOAL IS REACHED")
            current.displaysolution()
            return

        for action in ['uptilea', 'uptileb', 'downtilea', 'downtileb', 'lefttilea', 'lefttileb', 'righttilea', 'righttileb']:
            new_state = copy.deepcopy(current)
            if getattr(new_state, action)() and tuple(map(tuple, new_state.curr)) not in closed_set:
                new_state.level = current.level +1
                new_state.parent = current
                open_stack.put(new_state)
                
        # while open_stack.qsize()>3:
        #     open_stack.get(-1)

    print("GOAL NOT REACHED")

        
        
        


def main():
    #can be 1D or 2D Array
    initial=[[0,3,6],[1,2,0],[4,5,7]]
    goal=[[1,2,3],[4,5,6],[7,0,0]]
    p=puzzle(initial,goal)
    #Testing all moves and constraints--done in previous file
    #steepesthill(p)
    #bestfs(p)
    astar(p)#leading to issue
    
    #try variation -- with water jug and also 8 puzzle with 3 missing and euclidian or other heuristic
    #in beam search when to remove the excess element -- each time a new one is added?
main()

#all actions done
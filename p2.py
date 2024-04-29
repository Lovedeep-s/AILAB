from queue import PriorityQueue
import copy

class puzzle(object):
    def __init__(self,initial,goal):
        self.parent=None
        self.curr=initial
        self.level=0
        self.empty=self.getemptyindex()
        #for ease
        self.stateno=1
        self.empty1=self.empty[0]
        self.empty2=self.empty[1]
        self.goal=goal
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
    def displaysolution(self):
        print("--------SOLUTION--------")
        while self.parent!=None:
            print("STATE ",self.stateno)
            self.display_state()
            self=self.parent
        print("STATE ",self.stateno)
        self.display_state()
                
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
    def heursitic3(self):
        d=0
        val=self.curr[i][j]
        for i in range(3):
            for j in range(3):
                d+=((i-self.getxindex(val))**2+(j-self.getyindex(val))**2)
        return d
    def compare(self,p2):
        for i in range(3):
            for j in range(3):
                if self.curr[i][j]!=p2.curr[i][j]:
                    return False
        return True
    def __lt__(self,other):
        return self.level-(self.heuristic1())<other.level-(other.heuristic1())
    
    def sortparameter(self):
        return self.level-self.heuristic1()
        
closed_list=[]
def checkclosed(p1):
    for node in closed_list:
        if node.compare(p1):
            print("INSIDE CLOSED")
            return True
    return False
def beamfs(p):
    open_stack = PriorityQueue()
    #open_stack=open_stack[0:3]# Initialize the priority queue
    open_stack.put(p)  # Define the closed list
    while not open_stack.empty():
        
        current = open_stack.get()
        print("CURRENT STATE")
        current.display_state()
        closed_list.append(current)
        if current.isgoalreached():
            current.display_state()
            current.displaysolution()
            break
        for action in ['uptilea', 'uptileb', 'downtilea', 'downtileb', 'lefttilea', 'lefttileb', 'righttilea', 'righttileb']:
            new_state = copy.deepcopy(current)
            if getattr(new_state, action)() and checkclosed(new_state) == False:
                new_state.parent = current
                new_state.stateno += 1
                new_state.display_state()
                open_stack.put(new_state)
                if new_state.isgoalreached():
                    new_state.displaysolution()
                    break
            else:
                del new_state
        print(open_stack.qsize())
        if (open_stack.qsize())>3:
            temp =[ ]
            for i in range(3):
                temp.append(open_stack.get())
            while not open_stack.empty():
                h = open_stack.get()
            for i in range(3):
                open_stack.put(temp.pop())
        print(open_stack.qsize())
    if not current.isgoalreached():
        print("GOAL NOT REACHABLE")     

def main():
    #can be 1D or 2D Array
    initial=[[0,3,6],[1,2,0],[4,5,7]]
    goal=[[1,2,3],[4,5,6],[7,0,0]]
    p=puzzle(initial,goal)
    #Testing all moves and constraints--done in previous file
    #steepesthill(p)
    #bestfs(p)
    #astar(p)
    beamfs(p)
    
    #try variation -- with water jug and also 8 puzzle with 3 missing and euclidian or other heuristic
    #in beam search when to remove the excess element -- each time a new one is added?
main()

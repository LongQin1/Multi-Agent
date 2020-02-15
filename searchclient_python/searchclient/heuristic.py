from abc import ABCMeta, abstractmethod
from state import State
import math
from collections import deque

class Heuristic(metaclass=ABCMeta):
    def __init__(self, initial_state: 'State',goals):
        self.boxes = initial_state.boxes
        self.goals = goals
    
    def is_there_immediate_neighbour(self,goal, row, col):
        if row+1 < State.MAX_ROW: #we are still on the board
            box_test= self.boxes[row+1][col]
            goal_test= self.goals[row+1][col]
            if (box_test is not None) and (goal == box_test.lower()) and (goal_test is None or goal_test != box_test.lower()):
                return True
        if row-1 >= 0: #we are still on the board
            box_test= self.boxes[row-1][col]
            goal_test= self.goals[row-1][col]
            if (box_test is not None) and (goal == box_test.lower()) and (goal_test is None or goal_test != box_test.lower()):
                return True 
        if col+1 < State.MAX_COL: #we are still on the board
            box_test= self.boxes[row][col+1]
            goal_test= self.goals[row][col+1]
            if (box_test is not None) and (goal == box_test.lower()) and (goal_test is None or goal_test != box_test.lower()):
                return True
        if col-1 >= 0: #we are still on the board
            box_test= self.boxes[row][col-1]
            goal_test= self.goals[row][col-1]
            if (box_test is not None) and (goal == box_test.lower()) and (goal_test is None or goal_test != box_test.lower()):
                return True
        return False
    
    def GetDistance(self,goal,queue,goal_row,goal_col):
        p = queue.popleft()
        row = p[0]
        col = p[1]
        if self.is_there_immediate_neighbour(goal,row,col):
            return math.sqrt((goal_row-row)**2+(goal_col/col)**2)
        else:
            if row+1 < State.MAX_ROW:
                queue.append([row+1,col]) 
            if row-1 >= 0:
                queue.append([row-1,col]) 
            if col+1 < State.MAX_COL:
                queue.append([row,col+1]) 
            if col-1 >= 0:
                queue.append([row,col-1]) 
            self.GetDistance(self,goal,queue,goal_row,goal_col)
        


    def h(self, state: 'State') -> 'int':
    
        r=0
        for row in range(State.MAX_ROW):
            for col in range(State.MAX_COL):
                goal = self.goals[row][col]
                box = self.boxes[row][col]
                if goal is not None:
                    if box is not None and goal == box.lower():
                        r+=-100 #We might want to increase the weight of these
                        
                    else: # in goal but with no matching box.
                        queue= deque()
                        queue.append([row,col])
                        r += self.GetDistance(goal,queue,row,col)
        return r                                
    
    @abstractmethod
    def f(self, state: 'State') -> 'int': pass
    
    @abstractmethod
    def __repr__(self): raise NotImplementedError


class AStar(Heuristic):
    def __init__(self, initial_state: 'State',goals):
        super().__init__(initial_state,goals)
    
    def f(self, state: 'State') -> 'int':
        return state.g + self.h(state)
    
    def __repr__(self):
        return 'A* evaluation'


class WAStar(Heuristic):
    def __init__(self, initial_state: 'State', w: 'int',goals):
        super().__init__(initial_state,goals)
        self.w = w
    
    def f(self, state: 'State') -> 'int':
        return state.g + self.w * self.h(state)
    
    def __repr__(self):
        return 'WA* ({}) evaluation'.format(self.w)


class Greedy(Heuristic):
    def __init__(self, initial_state: 'State',goals):
        super().__init__(initial_state,goals)
    
    def f(self, state: 'State') -> 'int':
        return self.h(state)
    
    def __repr__(self):
        return 'Greedy evaluation'


from abc import ABCMeta, abstractmethod
from state import State


class Heuristic(metaclass=ABCMeta):
    def __init__(self, initial_state: 'State',goals):
        # Here's a chance to pre-process the static parts of the level.
        self.boxes = initial_state.boxes
        self.goals=goals
        self.rows = initial_state.agent_row
        self.columns = initial_state.agent_col
        pass
    
    def is_there_immediate_neighbour(self,goal, row, col):
        if row+1 < State.MAX_ROW: 
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
        if col-1 >= 0: #we are still on the board
            if row-1 >= 0:
                box_test= self.boxes[row-1][col-1]
                goal_test= self.goals[row-1][col-1]
                if (box_test is not None) and (goal == box_test.lower()) and (goal_test is None or goal_test != box_test.lower()):
                    return True
            if row+1 < State.MAX_ROW:
                box_test= self.boxes[row+1][col-1]
                goal_test= self.goals[row+1][col-1]
                if (box_test is not None) and (goal == box_test.lower()) and (goal_test is None or goal_test != box_test.lower()):
                    return True            
        if col+1 < State.MAX_COL: #we are still on the board
            if row-1 >= 0:
                box_test= self.boxes[row-1][col+1]
                goal_test= self.goals[row-1][col+1]
                if (box_test is not None) and (goal == box_test.lower()) and (goal_test is None or goal_test != box_test.lower()):
                    return True
            if row+1 < State.MAX_ROW:
                box_test= self.boxes[row+1][col+1]
                goal_test= self.goals[row+1][col+1]
                if (box_test is not None) and (goal == box_test.lower()) and (goal_test is None or goal_test != box_test.lower()):
                    return True
        return False
    
    def h(self, state: 'State') -> 'int':
        r=0 # assigning values for boxes in goal 
        for row in range(State.MAX_ROW):
            for col in range(State.MAX_COL):
                goal = self.goals[row][col]
                box = self.boxes[row][col]
                if goal is not None and box is not None and goal == box.lower():
                    r+=1 # We might want to increase the weight of these
        # assign value based on distance from boxes to empty goals.
        r=0
        for row in range(State.MAX_ROW):
            for col in range(State.MAX_COL):
                goal = self.goals[row][col]
                box = self.boxes[row][col]
                if goal is not None:
                    if box is not None and goal == box.lower():
                        r+=1000 #We might want to increase the weight of these
                        
                    else: # in goal but with no matching box.
                        d=0 #distance searched from the goal
                        while(True):  
                            if (is_there_immediate_neighbour(self,goal, row, col)):
                                break
#                            else:
 #                               d+=1
  #                              if row+1 < State.MAX_ROW: 
   #                                 if(is_there_immediate_neighbour(self,goal,row+1, col)):
    #                                    break
     #                           if row-1 >= 0: 
      #                              if(is_there_immediate_neighbour(self,goal,row-1, col)):
       #                                 break
        #                        if col+1 < state.MAX_COL: 
         #                           if(is_there_immediate_neighbour(self,goal,row, col+1)):
          #                              break
           #                         if row+1 < State.MAX_ROW:
            #                            if(is_there_immediate_neighbour(self,goal,row+1, col+1)):
             #                               break
              #                      if row-1 >=0:
               #                         if(is_there_immediate_neighbour(self,goal,row-1, col+1)):
                #                            break                                       
                 #               if col-1 >= 0: 
                  #                  if(is_there_immediate_neighbour(self,goal,row, col-1)):
                   #                     break
                    #                if row+1 < State.MAX_ROW:
                     #                   if(is_there_immediate_neighbour(self,goal,row+1, col-1)):
                      #                      break
                       #             if row-1 >= 0:
                        #                if(is_there_immediate_neighbour(self,goal,row-1, col-1)):
                         #                   break                                
                                
                                
                                

                                
    
    @abstractmethod
    def f(self, state: 'State') -> 'int': pass
    
    @abstractmethod
    def __repr__(self): raise NotImplementedError


class AStar(Heuristic):
    def __init__(self, initial_state: 'State'):
        super().__init__(initial_state)
    
    def f(self, state: 'State') -> 'int':
        return state.g + self.h(state)
    
    def __repr__(self):
        return 'A* evaluation'


class WAStar(Heuristic):
    def __init__(self, initial_state: 'State', w: 'int'):
        super().__init__(initial_state)
        self.w = w
    
    def f(self, state: 'State') -> 'int':
        return state.g + self.w * self.h(state)
    
    def __repr__(self):
        return 'WA* ({}) evaluation'.format(self.w)


class Greedy(Heuristic):
    def __init__(self, initial_state: 'State'):
        super().__init__(initial_state)
    
    def f(self, state: 'State') -> 'int':
        return self.h(state)
    
    def __repr__(self):
        return 'Greedy evaluation'


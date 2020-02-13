from abc import ABCMeta, abstractmethod


class Heuristic(metaclass=ABCMeta):
    def __init__(self, initial_state: 'State',goals):
        # Here's a chance to pre-process the static parts of the level.
        self.boxes = initial_state.boxes
        self.goals=goals
        self.rows = initial_state.agent_row
        self.columns = initial_state.agent_col
        pass
    
    
    def h(self, state: 'State') -> 'int':
        r=0 # assigning values for boxes in goal 
        for row in range(state.MAX_ROW):
            for col in range(state.MAX_COL):
                goal = self.goals[row][col]
                box = self.boxes[row][col]
                if goal is not None and box is not None and goal == box.lower():
                    r+=1 # We might want to increase the weight of these
        # assign value based on distance from boxes to empty goals.
        r=0
        for row in range(state.MAX_ROW):
            for col in range(state.MAX_COL):
                goal = self.goals[row][col]
                box = self.boxes[row][col]
                if goal is not None
                    if box is not None and goal == box.lower():
                        r+=1000 #We might want to increase the weight of these
                    else:
                        if 
                            self.boxes[][]
        return r
    
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


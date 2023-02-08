# This file is for the interface output, their revlevants and values 
import numpy as np
import random

def get_random_relevance(relevance_range: tuple): 
    return random.uniform(*relevance_range)

RELEVANCE = {
    "high": (1, 1), 
    "mid": (0, 0), 
    "low": (0, 0), 
    "irrelevant": (0.0, 0), 
    "null": (0, 0)
}

class Interface(object): 
    
    def __init__(self, relevance='irrelevant', current_value=0, id=None) -> None:
        self.relevance = relevance
        self.current_value = current_value
        self.id = id

    def vector(self)->np.array:
        return np.array([1])
    
    def get_relevance_nbr(self) -> float: 
        if self.relevance in RELEVANCE.keys(): 
            return get_random_relevance(RELEVANCE[self.relevance])
    
        return 0
        



class SwitchInterface(Interface): 

    def __init__(self, relevance=0,current_value=0,id=1, on_value=1, off_value=0) -> None:
        super().__init__(relevance=relevance, current_value=current_value, id=id)
        self.on_value = on_value
        self.off_value = off_value

    def vector(self) -> np.array: 
        return np.array([self.relevance,self.current_value, self.on_value, self.off_value])

class SliderInterface(Interface): 

    def __init__(self, relevance=0,current_value=0,id=2, min_value=0, max_value=1, step_value=0.1) -> None:
        super().__init__(relevance=relevance,current_value=current_value, id=id)
        self.min_value=min_value
        self.max_value=max_value
        self.step_value=step_value

    
    def vector(self) -> np.array:
        return np.array([self.relevance,self.current_value,self.min_value, self.max_value, self.step_value])

class ColorchooserInterface(Interface): 

    def __init__(self, relevance=0, current_value=0,id=3, color_value=0) -> None:
        super().__init__(relevance, current_value,id=id)
        self.color_value = color_value
    
    def vector(self) -> np.array:
        return np.array([self.relevance, self.current_value, self.color_value])

class StateInterface(Interface): 
    
    def __init__(self, relevance=0, current_value=0,id=4, state=0, interpreter=0) -> None:
        super().__init__(relevance, current_value,id=id)
        self.state = state
        self.interpreter = interpreter
    
    def vector(self) -> np.array:
        return np.array([self.relevance, self.current_value, self.state, self.interpreter])
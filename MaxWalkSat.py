__author__ = 'Vamshi Guduguntla'
__copyright__ = "NA"
__license__ = "NA"
__version__ = "1.0"

from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,numpy as np

class MWS:
    
    """
    :param max_tries                     - maximum retries
    :param max_changes                   - maximum iterations
       
    :func  mutate_in_a_dimension         - A function mutates the candidate solution in one dimension
    :func  mutate_to_maximize            - A function mutates to maximize the objective by incremental steps
    :func  maxwalksat                    - Initiates the maxwalksat algorithm
    """
    
    
    def __init__(self,model,prob = 0.5):
        self.notation= """Notation:
        "?" - moved to a worse solution/ random jump
        "." - solution that does not change
        "+" - better solution using a local change along one dimension"""
        self.p = prob
        self.max_tries = 100
        self.max_changes = 50
        self.maxwalksat(model)
    
    def mutate_in_a_dimension(self,state):
        rand_index = random.randrange(0,model.num_decisions)
        temp = list(state)
        if self.p < random.random():
            temp[rand_index] = random.randrange(model.dec_low[rand_index],model.dec_high[rand_index])
            if model.contraint_ok(temp):
                return temp, "."
            else:
                return state,"?"
        else:
            temp = self.mutate_to_maximize(temp,rand_index)
            if temp == state:
                return temp,"."
            else:
                if model.function_value(temp) < model.function_value(state):
                    return temp,"+"
                else:
                    return temp,"?"
    
    
    def mutate_to_maximize(self,state,rand_index):
        increment = (model.dec_high[rand_index] - model.dec_low[rand_index])/model.steps
        temp = list(state)
        best = state
        for _ in range(model.steps):
            temp[rand_index] += increment
            model.evals += 1
            """if (model.function_value(temp) < model.function_value(best)) and model.contraint_ok(temp):
                best = list(temp)"""
            if model.contraint_ok(temp):
                best = list(temp)
        state = best
        return state
    
    
    def maxwalksat(self,model):
        model.reset_baseline()
        print("Minimizing ",model.name)
        print("Objective High :",model.obj_high)
        print("Objective Low  :",model.obj_low)
        print("\n")
        print(self.notation)
        print("\n")
        best_state = model.randomstate()
        for _ in range(self.max_tries):
            state = model.randomstate()
            display = str()
            for i in range(self.max_changes):
                if model.function_value(state) < model.threshold:
                    return state
                else:
                    new_state, symbol = self.mutate_in_a_dimension(state)
                display += symbol
                if(model.function_value(state)<model.function_value(best_state)):
                    best_state = state
                if(model.function_value(new_state)<model.function_value(best_state)):
                    best_state = new_state
            print(display,round(model.norm(best_state),5))
        print("\n Result Statistics: ")
        print(np.around(best_state,9),"f1+f2:",model.function_value(best_state),"Evals: ",model.evals)
        print("\n")

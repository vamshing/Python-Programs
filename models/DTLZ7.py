from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,numpy as np

__author__ = 'Vamshi Guduguntla'
__copyright__ = "NA"
__license__ = "NA"
__version__ = "1.0"


class DTLZ7:
    
    """
    :param num_decisions    - Number of decisions/dimension of the array
    :param num_objectives   - Number of objectives to evaluate (f1,f2,....)
    :param dec_high         - Max range of the decision
    :param dec_low          - Min range of the decision
    :param obj_high         - Max range of the objective
    :param obj_low          - Min range of the objective
    :param num_objectives   - Number of objectives to evaluate (f1,f2,....)
    :param evals            - Keeps the track of the number of evaluations
    
    :func  f1               - scores a candidate on first objective
    :func  f2               - scores a candidate on second objective
    :func  function_value   - A function that scores a candidate
    :func  constraint_ok    - A function that checks for constraints (none of Kursawe and Schaffer)
    :func  norm             - A function that computes the objective scores for each candidate(normalized)
    :func  reset_baseline   - Resets the baseline for obj_high and obj_low computation
    """
    
    def __init__(self,num_eval = 0.0,prob = 0.5,high = 10**6,low = -10**6):
        self.name = "DTLZ7"
        self.num_decisions = 10
        self.num_objectives = 2
        self.dec_high = [1 for _ in range(10)]
        self.dec_low = [0 for _ in range(10)]
        self.steps = 10
        self.evals = num_eval
        self.obj_high = high
        self.obj_low = low
        self.threshold = -100
        self.reset_baseline()
        self.threshold = self.obj_low
        
        
    def reset_baseline(self):
        high = -10**6
        low = 10**6
        for _ in range(1000):
            dec = self.randomstate()
            en = self.function_value(dec)
            
            if en > high:
                high = en
            if en < low:
                low = en
        
        self.obj_high = high
        self.obj_low = low
        
    def g(self,dec):
        return 1 + ((9.)/(self.num_decisions)) * np.sum(dec)
    
    def h(self,dec):
        return self.num_decisions - self.h_helper(dec)
        
    def h_helper(self,dec):
        sum = 0.
        for i in range(0,self.num_decisions - 1):
            sum += ((dec[i])/(1+self.g(dec))) * (1 + math.sin(3 * math.pi * dec[i]))
        return sum
            
        
    def f9(self,dec):
        return dec[self.num_decisions - 1]
    
    def f10(self,dec):
        return (1+self.g(dec)) * self.h(dec)
    
    def function_value(self,dec):
        return self.f9(dec) + self.f10(dec)
    
    def contraint_ok(self,dec):
        return True
        
    def randomstate(self):
        while True:
            dec = list()
            for low,high in zip(self.dec_low,self.dec_high):
                dec.append(random.uniform(low,high))
            if self.contraint_ok(dec):
                return dec   
    
    def norm(self,state):
        return (self.function_value(state) - self.obj_low)/(self.obj_high - self.obj_low)

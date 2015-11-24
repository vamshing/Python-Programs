from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,numpy as np

__author__ = 'Vamshi Guduguntla'
__copyright__ = "NA"
__license__ = "NA"
__version__ = "1.0"


class Simulated_Annealing:
    
    """
    Performs the simulated annealing algorithm
    
    :param   model  : The model to optimize
    :param   kmax   : max iterations
    :param   cooling: cooling constant
    :param   s0     : initial solution
    :param   s      : the current solution
    :param   sb     : best solution so far
    :param   e      : current energy
    :param   eb     : best energy so far
    :param   emax   : least energy possible(hard-coded as 0.0 here)
    :param   temp   : the ratio of k and kmax
    
    :func 
    
    :returns        : The best solution found so far(sb)
    
    :stop criteria  : when 'k' reaches the max_iterations or energy found is less than equal to emax
    
    comments        : emax is hard-coded as 0.0 
    """
    
    def __init__(self,model,val=False,kmax=1000,cooling=4):
        
        self.notation= """Notation:
        "!" - moved to a best solution ( globally)
        "?" - moved to a worse solution/ random jump
        "." - solution that does not change
        "+" - better solution using a local change along one dimension"""
        self.kmax    = kmax
        self.val = val
        self.cooling = cooling
        self.simulatedannealing(model)
        
    def probability_calculation(self,k,e,en):
        return math.e**(((e-en))/((1-(k/self.kmax)))**self.cooling)
        
 
    def simulatedannealing(self,model):
        model.reset_baseline()
        print("Minimizing ",model.name)
        print("Objective High :",model.obj_high)
        print("Objective Low  :",model.obj_low)
        print("\n")
        print(self.notation)
        print("\n")
        k = 0
        s = model.randomstate()
        e = model.function_value(s)
        sb = s
        eb = e
        sayline = ""
        
        while k < self.kmax-1:
            k += 1
            say = " ."
            sn = model.randomstate()
            en = model.function_value(sn)
            if en < eb:
                sb = sn
                eb = en
                say = " !"
            elif en < e:
                s = sn
                e = en
                say = " +"
            elif self.probability_calculation(k,e,en)>random.random():
                s = sn
                e = en
                say = " ?"
            sayline += say
            if k % 25 == 0:
                if (self.val==False):
                    print(sb,sayline)
                sayline = ""    
        
        print("\n Result Statistics: ")

        if (self.val == True):
            print(model.obj_high,model.obj_low)
        else:
            print('Best Solution: ',sb,'Best Energy: ',eb)
        print("\n")
        
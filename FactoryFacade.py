from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random,numpy as np

__author__ = 'Vamshi Guduguntla'
__copyright__ = "NA"
__license__ = "NA"
__version__ = "1.0"


for model in [Kursawe(),Osyczka2(),Schaffer()]:
    for optimizer in [MWS,Simulated_Annealing]:
        optimizer(model)
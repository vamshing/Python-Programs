
from __future__ import print_function, division
from time import strftime
from pprint import pprint
import math,random

# In[58]:

__author__ = 'Vamshi Guduguntla'
__copyright__ = "NA"
__license__ = "NA"
__version__ = "2.0"



# Osyczka2

# Function value
def function_value(dec):
    f1 = -(25*(dec[0]-2)**2 + (dec[1]-2)**2 + ((dec[2]-1)**2)*(dec[3]-4)**2 + (dec[4]-1)**2)
    f2 = dec[0]**2 + dec[1]**2 + dec[2]**2 + dec[3]**2 + dec[4]**2 + dec[5]**2
    return f1,f2 

def contraint_ok(dec):
    g1 =  dec[0] + dec[1]-2 >= 0 
    g2 =  6 - dec[0] - dec[1] >= 0
    g3 =  2 - dec[1] + dec[0] >= 0
    g4 =  2 - dec[0] + 3 * dec[1] >= 0
    g5 =  4 - (dec[2] - 3)**3 + dec[5] - 4 >= 0
    g6 =  (dec[4] - 3)**3 + dec[5] -4 >= 0 
    return g1 and g2 and g3 and g4 and g5


# In[ ]:




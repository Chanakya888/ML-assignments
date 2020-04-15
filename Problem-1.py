import pandas as pd
from matplotlib import pyplot as plt

import numpy as np
np.random.seed()

def rand_range(r1,r2):
    return np.random.randint(r1,r2)
def pick(l):
    return np.random.choice(l)

def dice_roller(start,throws):
    steps = []
    for i in range(0,throws):
        k = rand_range(1,7)
        if k == 2 or k==1:
            if start > 0:
                start-=1
            else:
                pass
        elif k == 3 or k == 4 or k == 5:
            start+=1
        elif k==6 :
            start+=rand_range(1,7)
        steps.append([k,start])


    return start
print(dice_roller(0,250))
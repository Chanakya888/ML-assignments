from math_stuff.randomfactory import rand_range
import pandas as pd
from matplotlib import pyplot as plt

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
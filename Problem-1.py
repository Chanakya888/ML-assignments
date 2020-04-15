import numpy as np
np.random.seed()

def rand_range(r1,r2):
    return np.random.randint(r1,r2)
def pick(l):
    return np.random.choice(l)
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

def dice_Stair(throws, weights, total_runs):
    Sixty_Plus = []
    for i in range(total_runs):
        dice_v = []
        step = 0
        for j in range(throws):
            dice = random.choices(range(1, 7), weights=weights)
            dice = dice[0]
            if step == 0:
                if dice == 1 or dice == 2:
                    dice_v.append(dice)
                    continue
            if dice == 1 or dice == 2:
                step -= 1
            elif dice == 3 or dice == 5 or dice == 4:
                step += 1

            while dice == 6:
                dice = random.randint(1, 6)
                if step == 0:
                    if dice == 1 or dice == 2:
                        break
                if dice == 1 or dice == 2:
                    step -= 1
                elif dice == 3 or dice == 5 or dice == 4:
                    step += 1
                print("6 Encountered Re-Rolling", end=', ')
            print("Step = ", step, "Dice = ", dice)
        print("Steps Reached At the end of {} Cycle = {}".format(i, step))
        if step > 60:
            Sixty_Plus.append(1)
        else:
            Sixty_Plus.append(0)

    print("We Moved above Sixty Step = ", Sixty_Plus.count(1), " and ",
          "We are Less Than Sixty Steps = ", Sixty_Plus.count(0))
    print(f"Probability ({}) Trials and {} Throws per trial = ",(total_runs, throws), Sixty_Plus.count(1) / 1000)


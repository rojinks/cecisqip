import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    c = [0,0]
    for i in range(0,len(a)):
        if(a[i]>b[i]):
            c[0] += 1
        elif(a[i]<b[i]):
            c[1] += 1
        else:
            continue
    return c

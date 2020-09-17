#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    k=[]
    c=0
    d=0
    k.append(a[0]-b[0])
    k.append(a[1]-b[1])
    k.append(a[2]-b[2])
    for i in k:
        if(i<0):
            c+=1
        elif(i>0):
            d+=1
    l=[d,c]
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

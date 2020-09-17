#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    k=n-1;
    for i in range(n):
        print(" "*k+"#"*(i+1))
        k-=1

if __name__ == '__main__':
    n = int(input())
    staircase(n)

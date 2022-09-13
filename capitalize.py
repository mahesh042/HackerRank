#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s): 
    word_list = s.split(' ')
    final = []

    for i in word_list:
        a = ('-'.join(i))
        b = a.split('-')
        b[0]=b[0].upper()
        c = ''.join(b)
        final.append(c)
        out = ' '.join(final)
    
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

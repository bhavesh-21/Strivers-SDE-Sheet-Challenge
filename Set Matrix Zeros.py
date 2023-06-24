from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    # l=[]
    s=set()
    m=len(matrix)
    n=len(matrix[0])
    for i in range(m):
        yes=False
        for j in range(n):
            if matrix[i][j]==0:
                s.add(j)
                # l.append(j)
                yes=True
        if yes:
            for k in range(n):
                matrix[i][k]=0
    # s=set(l)
    for i in range(m):
        for p in s:
            matrix[i][p]=0
    return matrix

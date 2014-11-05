#!/usr/bin/env python

import numpy as np

#user input
n = 5  #number of grears
D = 8  #minimum distance between the two cooperative grears

    #radius & costr 
R = [1, 3, 6, 2, 5]
C = [5, 6, 8, 3, 4]


def min_cost():
    final = list()
    
    for i in range(0,len(R)):
        cost = {}
        for j in range(0,len(R)):
            if(R[i]+R[j] >= D ):
                cost[j] = C[i]+C[j]
        # print i ,cost  #DEBUG
        if cost:
            final.append( min(cost,key=cost.get) +1)
        else:
            final.append(0)
    print final
    
    
if __name__ == "__main__":
    min_cost()
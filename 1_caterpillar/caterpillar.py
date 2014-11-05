#!/usr/bin/env python

#Generating caterpillar jump sequence
N = 10;
A = [2,4,5]

#Representation for the leaves 
L  = [1]* (N+1)
L[0] = 0;

for i in range(0,len(A)):
    tmp = A[i]
    j = 2
    while(tmp < N+1):
        #print tmp  #DEBUG
        L[tmp] = 0;
        j+=1;
        tmp = A[i] * j
        
    
print sum(L)
print L
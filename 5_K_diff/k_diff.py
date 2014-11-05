#!/usr/bin/env python

import argparse

#user input
def main():
    parser = argparse.ArgumentParser(description = "find numbers from set N that have difference of K")
    parser.add_argument('-i', action = 'store', dest = 'input_file', help = "Usage: ./k_diff.py -i <input_file>")
    args = parser.parse_args()
    
    if(not args.input_file):
        print "Input file name not provided Usage: ./k_diff -i <file_name>"
        return -1
    
    f = open(args.input_file)
    
    if(not f):
        print "Invalid Filename! Wrong path or does not exist"
        return -1
    
    lines = f.read().splitlines()
    #print lines #DEBUG
    # print lines[0] #DEBUG
    
    line1 = lines[0].split(" ")
    # print line1 #DEBUG
    N = int(line1[0])
    K = int(line1[1])
    
    if (N < 0 or N > 100000 or K < 0 or K > 1000000000):
        print "N or L Out of range: Error  :[N<=10^5] and [K>0 and K<10^9]"
        return -1
        
    
    #print N, K  #DEBUG
    
    setN = map(int,lines[1].split(" "))
    
    #print setN  DEBUG
    
    valid_pairs= list()
    
    for i in range(0, len(setN)):
        for j in range(0,len(setN)):
            diff = setN[i] -setN[j]
            if (diff == K):
                valid_pairs.append([i,j])
                
    #print valid_pairs  #DEBUG
    
    len_valid_pairs = len(valid_pairs)
    
    print len_valid_pairs

if __name__ == "__main__":
    main()
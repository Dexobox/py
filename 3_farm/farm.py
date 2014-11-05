#!/usr/bin/env python

#input from the user
import argparse
import math

def main():
    parser = argparse.ArgumentParser(description='Process some feilds and do cows and sheep')
    parser.add_argument('-i', action="store", dest="input_file",  help = "Usage: ./farm.py -i <input_file>")
    args = parser.parse_args()
    
    if(not args.input_file):
        print "No input file name provided <>"
        return False
    
    f = open(args.input_file)
    if not(f):
        print "Invalid File or path"
        return False
    
    lines = f.read().splitlines()
    
    print lines
    
    
    arr = [] 
    tmp = lines[0].split()
    print tmp
    for i in range(1,int(tmp[0])+1 ):
        arr.append(list(lines[i]))
    
    print arr
    
    #check adjacent
    numrows =  len(arr)
    numcols = len(arr[0])
    field_count = 0
    flag  =  False
    for x in range(0,numrows ):
        for y in range (0,numcols):
            if(arr[x][y] == 'Y'):
                field_count+=1
                arr[x][y] = field_count
                
                if(y > 0):
                    if(arr[x][y-1] > 0):
                        arr[x][y] = arr[x][y-1]
                        flag =  True
                if(x > 0):
                    if(arr[x-1][y] > 0):
                        arr[x][y] = arr[x-1][y]
                        flag = True
                if(flag):
                    flag = False
                    field_count-=1
            else:
                arr[x][y] = 0
    print arr            
    print field_count
    
    #total number of possible 
    
    total_combinations = math.factorial(field_count)/math.factorial(field_count-2)
    print "The number of total combinations possible with S and C are "+ str(total_combinations)
    print "Henc the number of comonations with even number of sheep is " +str(total_combinations/2 - 1)
    
if __name__ == "__main__":
    main()
#!/usr/bin/env python
import sys

#add your array inputs here and pass variable name as argument 
# e.g. ./maddiff.py arr
arr = [2,3,10,2,4,8,1]

def check_arg(value):
    try: 
        eval(value)
    except ValueError:
        print value + "array does not exist"
        return -1

def maxDifference(a):
    big = max(a)
    
    if(index(big) == 0):
        print "-1"
        return -1
        
    diff_list= list()    
        
    for i in range(0, index(big)):
        diff_list.append(big - a[i])
        
    print max(diff_list)
    return max(diff_list)


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print "Too less/few argumens , Usage: ./macdiff.py <array_var_name>"
        sys.exit(-1)
    
    if ( check_arg(sys.argv[1])  < 0):
        print "array "+sys.argv[1] +" is not defined"
        sys.exit(-1)
        
    a = eval(arr)
    maxDifference(a)
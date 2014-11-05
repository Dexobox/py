#!/usr/bin/env python
import sys

#fucntion with try block to check if given input string is a number
def check_num(value):
    try: 
        int(value)
        return 0
    except ValueError:
        return -1

#main function
def fizzbuzz():
    #argument parsing
    if(not len(sys.argv) == 2):
        print "or too many/few arguments Usage : ./fizzbuzz.py <N>, where N is lenth to which the fizzbuzz sequenc has to be generated "
        return -1
    
    if sys.argv[1] == 'h' or sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] == '-help':
        print "usage: ./fizzbuzz.py <N> , N here is lenth to which fizzbuzz sequence is to be calculated"
        return -1
    
    #check if input is an integer
    if( (check_num(sys.argv[1]) ) < 0 ):
        print "Invalid! Input is is not an intiger"
        return -1
        
    
    #convertign string number to int        
    N = int(sys.argv[1])
    
    if(N > 10000000):
        print "Error! N value out of range  [ N < 10^7 ] "
        return -1
    #print N
    
    mod_3 = False
    mod_5 = False
    
    for i in range (1,N+1):
        if(i % 5 == 0):
            mod_5 = True
        if(i % 3 == 0):
            mod_3 = True
        
        if(mod_3 and mod_5):
            print "FizzBuzz"
        else:
            if(mod_3):
                print "Fizz"
            if(mod_5):
                print "Buzz"
            else:
                if((not mod_3) and (not mod_5)):
                    print i
        mod_3 = False
        mod_5 = False

if __name__ == "__main__":
    fizzbuzz()
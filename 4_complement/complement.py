#!/usr/bin/env python
import sys
from bitstring import Bits
from bitstring import BitArray

def check_num(value):  #function to check if value is an integer
    try:
        value = int(value)
    except ValueError:
        print ("Not an intiger")
        pass

def main():
    if(not len(sys.argv) == 2):
        print "Usagecomplement.py <N>  ; where 0 <= N <= 100000"
        return
        
    
    #check if the input string argument is an number
    check_num(sys.argv[1])
    #convert the string input to an integer
    N = int(sys.argv[1])
    
    #check the range requirement for the integer
    if(N > 100000 or N < 0):
        print "Invalid Range 0 <= N <= 100000"
        return
    
    #get the binary length of the integer bin outs a string which is in the format '0bXXX..' Hence -2
    bin_len = len(bin(N))-2
    
    #generate bitarray strings for the numbers
    one = BitArray(uint = 1,length = bin_len)
    binary  = BitArray(uint = N, length = bin_len)
    
    #print binary.bin #DEBUG
    #
    #complement the bit array to get 1's complement
    complement = ~(binary)
    
    #print complement.bin  #DEBUG
    
    # OR one into the bitarray to get two's complement of the number
    complement |= one
    
    #print complement.bin #DEBUG
    
    #print out the result in unsigned integer format
    print complement.uint
    
        

if __name__ == "__main__":
        main()
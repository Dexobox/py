#!/usr/bin/env python

import argparse

def swap_end_char(x):
    x = list(x)
    tmp = x[0]
    x[0] =x[ len(x)-1 ]
    x[len(x)-1] = tmp
    #print x
    return "".join(x)
    
    
def swap_con_char(x, i, j):
    x = list(x)
    tmp = x[i]
    x[i] =x[j]
    x[j] = tmp
    return "".join(x)

def stringswap():
    parser = argparse.ArgumentParser(description = "This program does end character swaps and consecutive char swaps to map 2 strings and outputs the number of moves")
    parser.add_argument('-i', action = 'store', dest = 'input_file',help = 'Input File Usage ./stringswap.py -i <input_file_name + path>')
    args = parser.parse_args()
    
    if(not args.input_file):
        print "Input file not provided! Usage : ./stringswap -i <input_file_name+path>"
        return -2
    
    f = open(args.input_file)
    
    if(not f):
        print "Invalid Input File! Invalid file name and/or path. Exiting!"
        return -2
        
    lines = f.read().splitlines()
    print lines
    
    string1 = lines[0]
    string2 = lines[1]
    moves = 0
    
    if(len(string1) != len(string2) ):
        print "The input strings do not belong to the same superset"
        return -1
    
    if not (string1.isalpha() and string2.isalpha()):
        print "Invalid strings, non-alphapbets found "
        return -1
    
    if not(string1.islower() and string2.islower()):
        print "Invalid strings, all alphapbets are not lower case "
        return -1
    
    
    for i in range(0,len(string1)):
        if(string1[i]==string2[i]):
            continue
        if(string1[0] == string2[len(string2)-1]  and string1[len(string1)-1]==string2[0]):
            string2 = swap_end_char(string2)
            moves+=1
        if(string1 ==  string2):
            break
        search_char = string1[i]
        try:
            findex = string2.index(search_char)
            reindex = string2.rindex(search_char)
            if( findex < (len(string2) - reindex)):
                print findex, len(string2)-reindex
                index = findex
            else:
                index = reindex
            if(string2.index(string2[i]) == len(string2)/2):
                index = reindex
            string2 = swap_con_char(string2, i, index)
            moves +=abs(index - i)
            print index, i
            print moves    
            print string2
        except ValueError:
            print "The strings do not match(do not have the same set of characters)"
            return -1
        
        
    print string2    
    print moves
    

if __name__ == "__main__":
    stringswap()
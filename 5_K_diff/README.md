
##Problem statement

    K Difference
    Given N numbers , [N<=10^5] we need to count the total pairs of numbers which have a difference of K. 
    [K>0 and K<10^9]. The solution should have as low of a computational time complexity as possible. 

    Input Format:
    1st line contains N & K (integers).
    2nd line contains N numbers of the set. All the N numbers are assured to be distinct.
    
    Output Format:
    One integer saying the no of pairs of numbers that have a diff K.
    
    Sample Input #00:
    5 2
    1 5 3 4 2
    
    Sample Output #00:
    3
    Explanation:
    The possible pairs are (5,3), (4,2) and (3,1).
     
     
    Sample Input #01:
    10 1
    363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 491595254 879792181 1069262793 
     
    Sample Output #01:
    0
     
    Explanation:
    There are no such pairs with the difference of 1.
     
    Read input from STDIN and write output to STDOUT. 

##Source 

    Hacker_Rank
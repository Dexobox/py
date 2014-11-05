
##Problem statement

    You need to set up two gears for two parts in a machine, parts A and B. The distance between A and B is equal to D. 
    There are n types of gears. Every ith gear is associated with (Ri, Ci) , where Ri and Ci indicate the radius and the cost of the gear respectively. 
    We can choose type i and type j gears if Ri + Rj >= D, because they will work cooperatively. 
    
    Iterating through every gear (Ri, Ci), find the gear to pair with the current gear. The same gear can be used twice. Our goal is to find the pair which costs the least. If there are multiple solutions with the same cost, output the gear with the largest radius. And if this is a tie as well, then output the gear with the smallest index. If there are no gears to be paired and does not reach the minimum distance, D, print 0.
    Input:  (All the variable names below, represent integer values)
    n  D
    R1 R2 ... Rn
    C1 C2 ... Cn
    
    Output:
    T1 T2 ... Tn
    
    Constraints:
    1 <= n <= 1000000
    1 <= D, Ri, Ci <= 1,000,000,000
    All are integers.
    1 <= Ti <= n
    
    Sample Input:
    5 8
    1 3 6 2 5
    5 6 8 3 4
    
    Sample Output:
    0 5 4 3 5
    
    Explanation:
    For type (1, 5): meet the requirement: {}.                                  Output 0. 
    For type (3, 6): meet the requirement: {(6, 8), (5, 4)}.                    (5, 4) is the one with minimal cost, so type 5 is the choice. 
    For type (6, 8): meet the requirement: {(3, 6), (6, 8), (2, 3), (5, 4)}.    (2, 3) is the one with minimal cost, so type 4 is the choice. 
    For type (2, 3): meet the requirement: {(6, 8)}.                            (6, 8) is the one with minimal cost, so type 3 is the choice. 
    For type (5, 4): meet the requirement: {(3, 6), (6, 8), (5, 4)}.            (5, 4) is the one with minimal cost, so type 5 is the choice. 
    
    
##Source 

    Hacker_Rank
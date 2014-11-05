
##Problem statement

    Given an array of integers ,a, return the maximum difference of any pair of numbers such that the larger 
    integer in the pair occurs a higher index (in the array) than the smaller integer with which it is paired.
    Return -1 if you cannot find a valid pair satisfying all constraints.
 
    You are provided with a function maxDifference which takes in the array as a parameter. 
    You are required to return an integer which is the right answer. 
    The section of the program which parses the input and displays the output will be handled by us.
    Your task is to complete the body of the function 
    or method provided, and to return the correct output.
    Sample TestCases 

    Input #00:
    Array: { 2,3,10,2,4,8,1}

    Output #00:
    8

    Explanation:
    10 is the largest number in the array and 1 is the lowest number in the array.
    However, the index of 10 is lesser than 1 and doesn't satisfy the constraint given to us.
    Assuming that this is a zero indexed array, the correct answer is a[2] - a[0] = 10 - 2 = 8.
    The pair which we have picked, satisfies the given constraint, that the larger number
    in the pair should be positioned at a higher index position in the array.

    Input #01: 
    Array: {7,9,5,6,3,2}

    Output #01: 
    2

    Explanation: 
    The value of maxDifference is 9 - 7 = 2.
    9 occurs at Index = 1 and 7 occurs at Index = 0. This satisfies the given constraint that
    the larger integer in the pair occurs a higher index (in the array) than the smaller 
    integer with which it is paired.


##Source 

    Hacker_Rank

##Problem statement

    In a grid farm, every cell is either 'Y' or 'N'. 'Y' means the cell has grass in it, and 'N' means the cell is empty.  
    If two adjacent cells have grass, they will belong to a common field. The same applies if there are more than 2 adjacent cells with grass. 7
    That is, if cell X is adjacent to cell Y and cell Y is adjacent to cell Z, 
    then cell X will be considered adjacent to cell Z and they will lie in the same field. 
    If a cell doesn't have any adjacent cell with grass, then it will also be a field.
    Every field must feed one sheep or one cow. Each field of grass cannot be shared between cows and sheep. 
    If each field has one sheep or one cow, how many possible unique arrangements are there, such that there is an even number of sheep?

    Input:
    The first line contains R  (number of rows) and C (number of columns)
    Each of the next R lines contains a string with length equal to C, and the string is composed of 'Y' and/or 'N'.
    
    Output:
    S % 1000000007, S is an integer
    Constraint:
    1 <= R, C <= 5000
    Sample Input:
    3 4
    YNNY
    NYNY
    NYNN
    
    |----|----|----|----|
    | 1  |    |    |    |
    |----|----|----|  3 |
    |    |    |    |    |
    |----| 2  |----|----|
    |    |    |    |    |
    |----|----|----|----|
    
    
    Sample Output:
    4               << <output seems fake>
    Explanation:
    1. First Solution 
    1. Cow 
    2. Cow 
    3. Cow          << <this case assuming 0 sheel is even number of sheep>
    2. Second Solution 
    1. Cow 
    2. Sheep 
    3. Cow          << <1 shee is a odd set>
    3. Third Solution 
    1. Cow 
    2. Cow 
    3. Sheep        <<<same goes here>>
    4. Fourth Solution 
    1. Cow 
    2. Sheep       <<<seems like a valid solution>
    3. Sheep     
    
##Source 

    Hacker_Rank
#User function Template for python3
import math
class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        def rightmostSetBit(n):
            if n==0:
                return 0
            return math.log2(n & -n)+1
        if rightmostSetBit(m^n):
            return rightmostSetBit(m^n)
        else:
            return -1
        

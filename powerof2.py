#User function Template for python3

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        if (n == 0):
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
        return True

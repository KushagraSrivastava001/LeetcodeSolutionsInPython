
class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        count=0
        while n!=0:
            if n%2==1:
                return count+1
            else:
                n=n/2
            count+=1
        return 0

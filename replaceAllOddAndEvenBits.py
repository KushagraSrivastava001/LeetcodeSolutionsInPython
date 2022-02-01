class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here
        even_bit=n & 0xAAAAAAAA
        odd_bit=n & 0x55555555
        odd_bit=odd_bit<<1
        even_bit=even_bit>>1
        
        return (odd_bit | even_bit)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.swapBits(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends

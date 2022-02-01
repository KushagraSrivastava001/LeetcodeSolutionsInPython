class Solution:
    
    #Function to check if the number is sparse or not.
    def isSparse(self,n):
        #Your code here 
        count=0
        while n>0:
            if n%2==1:
                count+=1
            else:
                count=0
            if count>=2:
                return False
                break
            n=n>>1
        return True
                
                

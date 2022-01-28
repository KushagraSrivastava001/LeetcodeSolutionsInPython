class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        set1=set()
        sum1=0
        for i in range(n):
            sum1+=arr[i]
            if(arr[i]==0 or sum1==0 or sum1 in set1):
                return True
            else:
                set1.add(sum1)
        return False
                
            

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        total_sum=sum(A)
        left_sum=0
        for i,num in enumerate(A):
            total_sum=total_sum-num
            if total_sum==left_sum:
                return i+1
            left_sum+=num 
        return -1

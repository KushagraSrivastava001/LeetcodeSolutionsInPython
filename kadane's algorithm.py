class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        cursum=arr[0]
        maxi_sum=arr[0]
        for i in range(1,len(arr)):
            cursum=max(arr[i],arr[i]+cursum)
            maxi_sum=max(maxi_sum,cursum)
        return maxi_sum

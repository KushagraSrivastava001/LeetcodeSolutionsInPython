class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        count=0
        # Your Code Here
        for i in range(n):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    count+=1
        return count

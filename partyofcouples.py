
class Solution:
    def findSingle(self, N, arr):
        # code here
        xor=arr[0]
        for i in range(1,len(arr)):
            xor^=arr[i]
        return xor

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.findSingle(N, arr))

# } Driver Code Ends

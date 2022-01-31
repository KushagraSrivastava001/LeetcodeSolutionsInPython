
class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
	    for i in range(N):
	        i=0
	        while i<N:
	            left=i
	            right=min(i+K-1,N-1)
	            while left<right:
	                arr[left]=arr[right]
	                left+=1
	                right-=1
	        i+=K

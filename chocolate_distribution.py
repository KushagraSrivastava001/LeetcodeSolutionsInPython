#User function Template for python3
import sys
class Solution:

    def findMinDiff(self, A,N,M):
        if M==0 and N==0:
            return 0
        if N<M:
            return -1
        min_diff=sys.maxsize
        A.sort()
        first=0
        last=0
        i=0
        while(i+M-1<N):
            difference=A[i+M-1]-A[i]
            if difference<min_diff:
                min_diff=difference
                first=i
                last=i+M-1
            i+=1
        return (A[last]-A[first])
                
            
        
        

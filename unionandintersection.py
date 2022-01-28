#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        a=set(a)
        b=set(b)
        union=a.union(b)
        union=list(union)
        return len(union)
        
        #code here

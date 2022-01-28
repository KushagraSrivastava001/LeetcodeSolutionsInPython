
class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        A=set(A)
        B=set(B)
        C=set(C)
        L=A.intersection(B)
        R=C.intersection(L)
        R=list(R)
        R.sort()
        return R
        

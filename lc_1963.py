import math
class Solution:
    def minSwaps(self, s: str) -> int:
        sm=0
        for i in s:
            if i=='[':
                sm+=1
            elif sm:
                sm-=1
        return (sm+1)//2

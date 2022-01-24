class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for char in s:
            if char not in d:
                d[char]=1
            else:
                d[char]+=1
        for t_char in t:
            if t_char not in d or d[t_char]==0:
                return False
            else:
                d[t_char]-=1
        return True
                

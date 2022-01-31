class Solution:
    def lastIndex(self, s):
        index=-1
        for i in range(len(s)):
            if s[i]=='1':
                index=i
        return index
        

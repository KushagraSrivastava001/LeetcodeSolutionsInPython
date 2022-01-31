class Solution:

    def longestSubstrDistinctChars(self, S):
        # code here
        n=len(S)
        res=0
        for i in range(n):
            visited=[0]*(256)
            for j in range(i,n):
                if visited[ord(S[j])]==True:
                    break
                else:
                    res=max(res,j-i+1)
                    visited[ord(S[j])]=True
            visited[ord(S[i])]=False
        return res

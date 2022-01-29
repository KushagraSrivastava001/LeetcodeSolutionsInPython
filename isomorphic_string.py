class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(word):
            output,lookup=[],{}
            i=1
            for words in word:
                
                if words not in lookup:
                    lookup[words]=i
                    i+=1
                output.append(lookup[words])
            return output
        return helper(s)==helper(t)
                    

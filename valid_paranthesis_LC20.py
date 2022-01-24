class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={')':'(',']':'[','}':'{'}
        for i in s:
            if i in d:
                if not stack or stack[-1]!=d[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return not stack
                

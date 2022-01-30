class Solution:
    def removeConsecutiveCharacter(self, S):
        stack=[S[0]]
        for i in range(1,len(S)):
            if stack[-1]==S[i]:
                continue
            else:
                stack.append(S[i])
        return ''.join(stack)

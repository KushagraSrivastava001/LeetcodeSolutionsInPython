# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        charArray=S.split('.')
        start=0
        end=len(charArray)-1
        while start<end:
            charArray[start],charArray[end]=charArray[end],charArray[start]
            start+=1
            end-=1
        return '.'.join(charArray)

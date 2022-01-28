
class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        #code here
        if len(s1)!=len(s2):
            return 0
        s=s1+s1
        if s.count(s2)>0:
            return 1
        else:
            return 0

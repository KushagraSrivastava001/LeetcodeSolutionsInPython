class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        if len(str1)!=len(str2):
            return 0
        if len(str1)<=2:
            return str1==str2
        clock=''
        anticlock=''
        l=len(str1)
        clock=str1[2:]+str1[:2]
        anticlock=anticlock+str1[l-2:]+str1[:l-2]
        if str2==clock or str2==anticlock:
            return 1
        else:
            return 0

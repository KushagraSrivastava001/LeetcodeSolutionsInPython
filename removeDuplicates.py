#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		hashSet=set()
		res=""
		for i in S:
		    if i not in hashSet:
		        res+=i
		    hashSet.add(i)
		return res
		

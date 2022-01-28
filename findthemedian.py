
class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
		if len(v)%2==1:
		    return v[len(v)//2]
		else:
		    mid1=v[(len(v)//2)-1]
		    mid2=v[(len(v)//2)]
		    t=(mid1+mid2)//2
		    return t
		    

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency=len(nums)/3
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        result=[]
        for key in d.keys():
            if d[key]>frequency:
                result.append(key)
        return result
        

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr=[]
        k=len(nums)
        for i in range(k):
            start=i+1
            end=k-1
            res=0-nums[i]
            while start<end:
                if nums[start]+nums[end]+nums[i]==0 and [nums[start],nums[end],nums[i]] not in arr:
                    arr.append([nums[start],nums[end],nums[i]])
                elif nums[start]+nums[end]>res:
                    end-=1
                else:
                    start+=1
            
        return arr
            

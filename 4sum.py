class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        arr=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                start=j+1
                end=len(nums)-1

                while start<end:
                    currentSum=nums[i]+nums[j]+nums[start]+nums[end]
                    if currentSum ==target and [nums[i],nums[j],nums[start],nums[end]] not in arr:
                        arr.append([nums[i],nums[j],nums[start],nums[end]])
                    elif currentSum>target:
                        end-=1
                    else:
                        start+=1
        return arr

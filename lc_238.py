class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ones=[1]*len(nums)
        cf=1
        for i in range(len(nums)):
            ones[i]=ones[i]*cf
            cf=cf*nums[i]
        cf=1
            
        for i in range(len(nums)-1,-1,-1):
            ones[i]=ones[i]*cf
            cf=cf*nums[i]
        return ones
            

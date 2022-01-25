class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited={}
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited[nums[i]]=i
            else:
                index_diff=abs(i-visited[nums[i]])
                if index_diff<=k:
                    return True
                visited[nums[i]]=i
        return False

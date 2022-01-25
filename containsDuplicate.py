ass Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited={}
        for num in nums:
            if num not in visited:
                visited[num]=True
            else:
                return True
        return False
        

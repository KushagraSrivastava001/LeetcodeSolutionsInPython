from heapq import heappush,heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        priorityqueue=[]
        for num in nums:
            heappush(priorityqueue,num)
            
        while len(priorityqueue)>k:
            heappop(priorityqueue)
        
        
        return priorityqueue[0]

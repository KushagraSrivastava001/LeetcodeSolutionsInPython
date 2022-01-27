from heapq import heappush,heappop
class Solution:
    def kthSmallest(self,arr, l, r, k):
        priorityqueue=[]
        for array in arr:
            heappush(priorityqueue,array)
        for i in range(k-1):
            heappop(priorityqueue)
        return priorityqueue[0]

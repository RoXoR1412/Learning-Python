#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import List
from heapq import heapify, heappop, heappush
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return sorted(nums, reverse=True)[k-1]
        min_heap=[]
        for num in nums:
            if len(min_heap)<k:
                heappush(min_heap,num)
            elif num> min_heap[0]:
                heappop(min_heap)
                heappush(min_heap,num)
            #print(min_heap)
        return min_heap[0]



        
# @lc code=end


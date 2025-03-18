#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
# @lc code=start
from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #print(Counter(nums).items())
        min_heap=[]
        for key,value in Counter(nums).items():
            if len(min_heap)<k:
                heappush(min_heap, (value,key))
            elif value> min_heap[0][0]:
                heappop(min_heap)
                heappush(min_heap, (value,key))
        return [x[1] for x in min_heap]

        
# @lc code=end


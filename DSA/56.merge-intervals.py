#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return  []
        intervals.sort(key=lambda x:x[0])
        merged=intervals[:1]
        for i in intervals[1:]:
            if i[0]<=merged[-1][-1]:
                merged[-1][-1]=max(merged[-1][-1],i[-1])
            else:
                merged.append(i)
        return merged



        
# @lc code=end


#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
from typing import List
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        merged=intervals[:1]
        for i in intervals[1:]:
            if i[0]<=merged[-1][-1]:
                merged[-1][-1]=max(merged[-1][-1],i[-1])
            else:
                merged.append(i)
        return merged
        
# @lc code=end


#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
from typing import List

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        end=intervals[0][1]
        count =0
        for i in intervals[1:]:
            if i[0]<end:
                count+=1
            else:
                end=i[1]
        return count
        
# @lc code=end


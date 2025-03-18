#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                prev_idx=stack.pop()
                result[prev_idx]=i-prev_idx
            stack.append(i)
        return result
        
# @lc code=end


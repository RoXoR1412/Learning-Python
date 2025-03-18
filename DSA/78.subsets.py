#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start=0, path=[]):
            output.append(path)
            for i in range(start,len(nums)):
                backtrack(i+1, path+nums[i:i+1])
        output = []
        backtrack()
        return output
        
# @lc code=end


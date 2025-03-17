#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
from typing import List
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=nums[0],nums[0]
        while True:
            slow,fast=nums[slow],nums[nums[fast]]
            if slow==fast:
                slow=nums[0]
                while slow!=fast:
                    slow,fast=nums[slow],nums[fast]
                return slow
        
# @lc code=end


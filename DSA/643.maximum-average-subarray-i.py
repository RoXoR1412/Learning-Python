#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
from typing import List
# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <k:
            return sum(nums)/len(nums)
        max_sum=sum(nums[:k])
        curr_sum=max_sum
        for i in range(k,len(nums)):
            curr_sum=curr_sum+nums[i]-nums[i-k]
            max_sum=max(max_sum,curr_sum)
        return max_sum/k
        
        
# @lc code=end


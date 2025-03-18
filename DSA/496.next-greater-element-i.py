#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
from typing import List
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, hashmap = [], {}
        for num in nums2:
            while stack and stack[-1] < num:
                hashmap[stack.pop()] = num
            stack.append(num)
        return [hashmap.get(num, -1) for num in nums1]

        
# @lc code=end


#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left=0
        right=len(nums)-1
        if nums[right]>nums[0]:
            return nums[0]
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[mid]>nums[0]:
                left=mid+1
            else:
                right=mid-1
        return -1
        
# @lc code=end


#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        row=0
        col=len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col]==target:
                return True
            if matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False
# @lc code=end


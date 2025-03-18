#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List
from unittest import result
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def create_board():
            return [["." for _ in range(n)] for _ in range(n)]
        def is_safe(row,col):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
                if board[i][j]=="Q":
                    return False
            for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
                if board[i][j]=="Q":
                    return False
            return True
        def backtrack(row=0):
            if row ==n:
                solution =[''.join(row) for row in board]
                result.append(solution)
                return
            for col in range(n):
                if is_safe(row,col):
                    board[row][col]="Q"
                    backtrack(row+1)
                    board[row][col]="."
        board=create_board()
        result=[]
        backtrack(0)
        return result
        
# @lc code=end


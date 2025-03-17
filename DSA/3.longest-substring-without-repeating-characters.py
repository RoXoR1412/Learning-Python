#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        start=0
        max_len=0

        for i in range(1,len(s)):
            if s[i] in s[start:i]:
                max_len=max(max_len,i-start)
                start=s[start:i].index(s[i])+start+1
        return max(max_len,len(s)-start)
# @lc code=end


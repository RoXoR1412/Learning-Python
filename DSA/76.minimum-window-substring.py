#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        if len(s) == 1 and len(t) == 1:
            return s if s == t else ""
        
        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            print(f"Right: {r}, Character: {character}, Window Counts: {window_counts}, Formed: {formed}")
            
            while l <= r and formed == required:
                character = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                
                print(f"Left: {l}, Character: {character}, Window Counts: {window_counts}, Formed: {formed}, Ans: {ans}")
                
                l += 1
            
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# Example usage:
sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
# @lc code=end


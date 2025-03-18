#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while prev.next and prev.next.next:
            current=prev.next
            next=prev.next.next
            prev.next=next
            current.next=next.next
            next.next=current
            prev=current
        return dummy.next
        
# @lc code=end


#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        for _ in range(left-1):
            prev=prev.next
        current=prev.next
        next=None
        for _ in range(right-left):
            next=current.next
            current.next=next.next
            next.next=prev.next
            prev.next=next
        return dummy.next
        
# @lc code=end


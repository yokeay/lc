# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumpy = ListNode(-1, head)
        current = dumpy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            
            first.next = second.next
            second.next = first
            current.next = second
            # first与second的部分已经挪完了所以继续下一个，所以还是从first开始
            current = first
        return dumpy.next


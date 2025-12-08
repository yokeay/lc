# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        header = ListNode(0)
        al = ListNode(-1)
        header.next = al
        while head:
            lst.append(head.val)
            head = head.next
        lst.reverse()
        for number in lst:
            al.next = ListNode(number)
            al = al.next
        return header.next.next
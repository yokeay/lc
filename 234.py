# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:

    def __init__(self, val=0):
        self.val = val
        self.next = None

    def next(self, val):
        self.next = ListNode(val)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack == stack[::-1]


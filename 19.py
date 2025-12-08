# Definition for singly-linked list.
from typing import Optional
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 先存储起来
        dict = []
        while head:
            dict.append(head)
            head = head.next
        number = len(dict)
        if n > number:
            return []
        target_index = number - n
        if target_index == 0:
            return dict[target_index].next
        dict[target_index - 1].next = dict[target_index].next
        return dict[0]
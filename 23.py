# Definition for singly-linked list.




from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        data_dict = []
        for head in lists:
            while head:
                data_dict.append(head.val)
                head = head.next
        lst = sorted(data_dict)
        head = ListNode()
        cache = ListNode(0, head)
        for val in lst:
            head.next = ListNode(val= val)
            head = head.next
        return cache.next.next
        
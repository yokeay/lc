# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print_list(self,head):
        cur = head
        res = []
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        print(" -> ".join(res))
    
    def build_list(self,*nums):
        """接受任意数量的数字参数，构造链表"""
        if not nums:
            return None
        head = ListNode(nums[0])
        cur = head
        for v in nums[1:]:
            cur.next = ListNode(v)
            cur = cur.next
        return head


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        po = dummy
        for _ in range(left - 1):
            po = po.next
        cur = po.next
        pre = None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        po.next.next = cur
        po.next = pre
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    n = ListNode()
    head = n.build_list(1,2,3,4,5)
    n.print_list(head)
    res = s.reverseBetween(head, 2, 4)
    n.print_list(res)
    head = n.build_list(1)
    res = s.reverseBetween(head, 1, 1)
    n.print_list(res)
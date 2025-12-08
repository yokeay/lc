# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # 工具函数：把 Python 列表变成链表
def build_list(nums):
    dummy = ListNode(0)
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

# 工具函数：打印链表
def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cache = head
        while list1 and list2:
            if list1.val > list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next
        head.next = list1 if list1 else list2
        return cache.next
            

if __name__ == '__main__':
    # ====== 测试用例 ======
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    s1 = Solution()
    res = s1.mergeTwoLists(l1,l2)
    print_list(res)
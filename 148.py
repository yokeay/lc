# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # 1. 收集所有节点（注意是节点本身，不是值）
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        # 2. 按节点的 val 排序
        nodes.sort(key=lambda node: node.val)

        # 3. 重新连接
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None  
        # 最后一个指向 None

        # 4. 返回新的头节点
        return nodes[0]

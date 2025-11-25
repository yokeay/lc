# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Docstring for addTwoNumbers
            需要考虑的问题如下：
            首先，非负整数： 0 或者正整数
            其次，逆序 低位在前，高位在后
            最后，长度 相加的两个链表长度可能不尽相同，因此要从最短的那个开始遍历遍历完了之后如果存在和进位则进位至长的链表的下一位数值
            如果链表长度相同，只需要按需遍历相加进位即可
        :param self: Description
        :param l1: Description
        :type l1: Optional[ListNode]
        :param l2: Description
        :type l2: Optional[ListNode]
        :return: Description
        :rtype: Any
        '''
        if not l1 or not l2:
            return None
        # 初始化结果集的头节点
        res_head = ListNode(-1, None)
        # 先考虑一个节点的情况
        if not l1.next:
            if not l2:
                return l1
            if not l2.next:
               first_node_val, second_node_val = abs((l1.val + l2.val)-10), 1 if (l1.val + l2.val) > 10 else (l1.val + l2.val), None
               first_node = ListNode(first_node_val, None)
               if not second_node_val:
                   return first_node
               else:
                   first_node.next = ListNode(second_node_val, None)
                   return first_node
        if not l2.next:
            if not l1:
                return l2
            if not l1.next:
               first_node_val, second_node_val = abs((l1.val + l2.val)-10), 1 if (l1.val + l2.val) > 10 else (l1.val + l2.val), None
               first_node = ListNode(first_node_val, None)
               if not second_node_val:
                   return first_node
               else:
                   first_node.next = ListNode(second_node_val, None)
                   return first_node
        # 再考虑不一样长度的情况
        additional = 0
        while l1 and l2:
            first_node_val, second_node_val = abs((l1.val + l2.val)-10), 1 if (l1.val + l2.val) > 10 else (l1.val + l2.val), None
            res_head.next = ListNode(first_node_val, None)
            if second_node_val:
              additional += second_node_val
            l1 = l1.next
            l2 = l2.next
        # 最后将additional给最后一个节点
        
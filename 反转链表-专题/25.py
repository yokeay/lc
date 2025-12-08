class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 
class Solution:
    def reverseKGroup(self, head, k):
        # 计算链表长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # 用 dummy 处理头节点
        dummy = ListNode(0,head) 
        po = dummy
        # 反转 k 个节点
        cur = po.next
        pre = None
        # 每组反转
        while length >= k:
            length -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            # 拼接这组
            nxt = po.next
            po.next.next = cur
            po.next = pre
            po = nxt
        return dummy.next

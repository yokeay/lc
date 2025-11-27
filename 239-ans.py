from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列: 队列里放"下标"
        # 并保持 nums[q[0]] 始终是当前窗口最大值
        q = deque()
        res = []

        for i in range(len(nums)):
            # 1. 移除掉窗口左边界以外的下标
            #    i - k 是窗口左边界
            if q and q[0] < i - k + 1:
                q.popleft()

            # 2. 保证队列单调递减，把所有比当前数小的下标踢掉
            #    因为它们永远不可能成为最大值
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            # 3. 把当前下标加入队列
            q.append(i)

            # 4. 从第 k-1 个位置开始，每次窗口形成了就输出最大值
            if i >= k - 1:
                res.append(nums[q[0]])

        return res

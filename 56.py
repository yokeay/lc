from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 结果
        res = []
        # 排序
        intervals.sort(key=lambda x: x[0])
        # 装载
        res.append(intervals[0])
        # 遍历
        for index in range(1, len(intervals)):
            if intervals[index][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[index][1])
            else:
                res.append([intervals[index][0], intervals[index][1]])
        return res
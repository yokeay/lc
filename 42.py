from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 接雨水 首先 要理解一个问题
        # 能存下来雨水是计算两个不相邻的柱子之间是否存在0高度的情况
        # 其次，水面最大高度不取决于最高的柱子而是这两个不相邻柱子之间较短的柱子也就是短板效应
        # 依次统计不相邻的柱子情况就可以得出结果了 
        left_index = 0
        right_index = len(height) - 1
        total = 0
        left_max = height[left_index]
        right_max = height[right_index]

        while left_index < right_index:
            if height[left_index] < height[right_index]:
                if height[left_index] >= left_max:
                    left_max = height[left_index]
                else:
                    total += left_max - height[left_index]
                left_index += 1
            else:
                if height[right_index] >= right_max:
                    right_max = height[right_index]
                else:
                    total += right_max - height[right_index]
                right_index -= 1
        return total
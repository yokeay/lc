from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 给定一个窗口大小,返回窗口范围内的最大数字
        # 最大数字可以直接用max来做
        # 窗口返回是每次循环遍历起始位置index + 窗口长度,所以窗口的起始位置 = [startIndex, startIndex+k-1]
        # 因为要使用窗口遍历整个nums, 所以要看窗口大小是否小于等于数组长度
        # 遍历次数等于len(nums) - k + 1
        if len(nums) == 1 or not nums:
            return nums
        loop_count = len(nums) - k + 1
        res = []
        max_value = max(nums[0:k])
        res.append(max_value)
        for i in range(1, loop_count):
            left_value, right_value = nums[i], nums[i+k-1]
            if left_value >= max_value:
                max_value = max(nums[i:i+k])
            if right_value >= max_value:
                max_value = right_value
            res.append(max_value)
        return res
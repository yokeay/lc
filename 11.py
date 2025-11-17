from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        max_area = 0
        while left_index < right_index:
            max_area = max(max_area, min(height[right_index] , height[left_index]) * (right_index - left_index))
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return max_area


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
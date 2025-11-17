class Solution:
    def threeSum(self, nums):
        nums.sort()
        length = len(nums)
        result = set()

        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            seen = set()

            for j in range(i+1, length):
                b = nums[j]
                c = target - b
                if c in seen:
                    result.add((nums[i], c, b))
                seen.add(b)
        return [list(i) for i in result]
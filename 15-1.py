class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            # 跳过重复 a
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            seen = set()

            for j in range(i+1, n):
                b = nums[j]
                c = target - b
                if c in seen:
                    res.add((nums[i], c, b))
                seen.add(b)

        return [list(t) for t in res]

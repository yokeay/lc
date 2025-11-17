class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        if len(s) < 2:
            return len(s)
        for right in range(len(s)):
            # 右指针扩展时，如果字符重复
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # 把当前字符加入窗口
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
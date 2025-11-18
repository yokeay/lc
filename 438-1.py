from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        if n < k:
            return []

        freq_p = [0] * 26
        freq_s = [0] * 26

        # 统计 p 的频率
        for ch in p:
            freq_p[ord(ch) - 97] += 1

        res = []
        left = 0

        for right in range(n):
            # 扩张窗口：加入 s[right]
            freq_s[ord(s[right]) - 97] += 1

            # 如果窗口长度超过 p_len，就缩小
            if right - left + 1 > k:
                freq_s[ord(s[left]) - 97] -= 1
                left += 1

            # 如果窗口长度正好 == k，看看是不是异位词
            if freq_s == freq_p:
                res.append(left)

        return res

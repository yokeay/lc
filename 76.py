from collections import Counter, defaultdict
from typing import Optional

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)           # 需要的字符频次
        window = defaultdict(int)   # 当前窗口的字符频次
        required = len(need)        # 需要满足的字符种类数
        valid = 0                   # 当前满足需求的字符种类数

        left = 0
        right = 0
        min_len = float('inf')
        ans_l = 0

        while right < len(s):
            c = s[right]
            right += 1
            # 增加窗口内字符计数
            if c in need:
                window[c] += 1
                # 当某字符计数刚好达到 need 要求时，valid +1
                if window[c] == need[c]:
                    valid += 1

            # 当窗口已满足所有字符需求时，尝试收缩左边以找到最小窗口
            while valid == required:
                # 更新答案
                if right - left < min_len:
                    min_len = right - left
                    ans_l = left

                # 准备收缩：移除左边字符
                d = s[left]
                left += 1
                if d in need:
                    # 移除后如果计数少于要求，则 valid 减一
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if min_len == float('inf') else s[ans_l: ans_l + min_len]

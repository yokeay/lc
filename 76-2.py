from collections import Counter, defaultdict
from typing import Optional

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        if len(t) == len(s):
            return s if t==s else ""
        
        left_index = 0
        right_index = 0
        need = Counter(t)
        reqired = len(need)
        valid = 0
        min_length = float('inf')
        window = defaultdict(int)
        ans_left_index = 0

        while right_index < len(s):
            current_char = s[right_index]
            right_index += 1
            if current_char in t:
                window[current_char] += 1
                # 当某字符计数刚好达到 need 要求时，valid +1
                if window[current_char] == need[current_char]:
                    valid += 1

            while valid == reqired:
                if right_index - left_index < min_length:
                    min_length = right_index - left_index
                    ans_left_index = left_index
                d = s[left]
                left += 1
                if d in need:
                    # 移除后如果计数少于要求，则 valid 减一
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if min_length == float('inf') else s[ans_left_index: ans_left_index + min_length]

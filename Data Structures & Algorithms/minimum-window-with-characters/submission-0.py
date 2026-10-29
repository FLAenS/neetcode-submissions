class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        have, required = 0, len(need)
        res_len = float('inf')
        res_l = 0
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            while have == required:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res_l = l
                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1
        return "" if res_len == float('inf') else s[res_l:res_l + res_len]
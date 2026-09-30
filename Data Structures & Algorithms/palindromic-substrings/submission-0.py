class Solution:
    def countSubstrings(self, s: str) -> int:
        def extend(l: int, r: int):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt
        res = 0
        for i in range(len(s)):
            res += extend(i, i)
            res += extend(i, i + 1)
        return res
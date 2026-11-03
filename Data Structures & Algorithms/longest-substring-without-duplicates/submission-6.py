class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        length, res = 0, 0
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                length += 1
                res = max(length, res)
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    length -= 1
                    l += 1
                l += 1
        return res
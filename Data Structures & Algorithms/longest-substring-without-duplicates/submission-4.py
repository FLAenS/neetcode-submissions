class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        maxlen = 0
        l = 0
        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l += 1
            res.add(s[r])
            maxlen = max(maxlen, len(res))
            r += 1
        return maxlen
        


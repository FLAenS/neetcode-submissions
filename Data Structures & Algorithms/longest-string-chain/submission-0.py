class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        dp = {}
        words.sort(key=len)
        for word in words:
            dp[word] = 1
            for k in range(len(word)):
                pred = word[:k] + word[k+1:]
                if pred in dp:
                    dp[word] = max(dp[word], dp[pred] + 1)
        return max(dp.values())

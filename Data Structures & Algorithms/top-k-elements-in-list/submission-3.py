class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]
        for i in cnt.items():
            bucket[i[1]].append(i[0])
        res = []
        num = 0
        for i in range(len(nums), -1, -1):
            for x in bucket[i]:
                res.append(x)
                num += 1
                if num == k:
                    return res

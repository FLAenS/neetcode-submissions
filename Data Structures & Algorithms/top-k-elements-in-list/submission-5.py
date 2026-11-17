class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep a min heap
        cnt = Counter(nums) # cnt (num: freq)
        b = [[] for i in range(len(nums) + 1)] # freq from 0 to len nums
        for num, freq in cnt.items():
            b[freq].append(num)
        res = []
        for freq in range(len(b) - 1, 0, -1):
            for num in b[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
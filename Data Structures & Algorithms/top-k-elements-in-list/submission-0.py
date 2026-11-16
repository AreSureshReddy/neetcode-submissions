class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
            
        return res
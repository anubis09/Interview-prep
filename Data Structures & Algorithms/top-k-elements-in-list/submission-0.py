class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for _ in range(len(nums)+1)]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num, freq in count.items():
            frequency[freq].append(num)
        
        res = []
        for i in range(len(frequency)-1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res
                


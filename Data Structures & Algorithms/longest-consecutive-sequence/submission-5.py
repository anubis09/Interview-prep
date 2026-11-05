class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_sequence = 0
        for n in numset:
            if n - 1 not in numset:
                seq_len = 1
                while n + seq_len in numset:
                    seq_len += 1
                longest_sequence = max(longest_sequence, seq_len)
        
        return longest_sequence
            
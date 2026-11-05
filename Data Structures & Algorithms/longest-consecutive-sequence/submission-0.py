class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        starters = [n for n in nums if n-1 not in lookup]
        longest_sequence = 0
        for starter in starters:
            seq_len = 1
            while starter + seq_len in lookup:
                seq_len += 1
            longest_sequence = max(longest_sequence, seq_len)
        
        return longest_sequence
            
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        cum_pref = 1
        for n in nums:
            res.append(cum_pref)
            cum_pref *= n
        
        cum_suf = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= cum_suf
            cum_suf*=nums[i]
        
        return res
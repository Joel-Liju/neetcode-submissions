class Solution:
    def rob(self, nums: List[int]) -> int:
        vals = [0] * len(nums)
        if len(nums) <= 2:
            return max(nums)
        
        vals[0] = nums[0]
        vals[1] = nums[1]

        for i, num in enumerate(nums):
            if i == 2:
                vals[i] = vals[i - 2] + num
            if i >= 3:
                vals[i] = max(vals[i-2], vals[i-3]) + num
        return max(vals)
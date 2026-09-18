class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        vals = [0] * len(nums)
        vals[0] = nums[0]

        for i in range(1, len(nums)):
            vals[i] = max(nums[i], vals[i - 1] + nums[i])
        return max(vals)
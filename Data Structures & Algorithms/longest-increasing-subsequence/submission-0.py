class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxSizes = [1] * len(nums)

        for i in range(1, len(nums)):
            j = i - 1

            while j > -1:
                if nums[j] < nums[i]:
                    maxSizes[i] = max(maxSizes[i], maxSizes[j] + 1)
                j -= 1
            # print(maxSizes)

        return max(maxSizes)
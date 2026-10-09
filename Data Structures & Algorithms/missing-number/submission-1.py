class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        flags = [False] * 1000
        maxVal = -1
        for num in nums:
            flags[num] = True
            maxVal = max(maxVal, num)
        for i, flag in enumerate(flags):
            if i > maxVal:
                break
            if not flag:
                return i
        return maxVal + 1
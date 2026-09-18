class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canJumpHere = [False] * len(nums)
        canJumpHere[0] = True


        for i in range(len(nums)):
            if canJumpHere[i]:
                for j in range(1, nums[i] + 1):
                    if i + j < len(nums):
                        canJumpHere[i + j] = True

        return canJumpHere[-1]
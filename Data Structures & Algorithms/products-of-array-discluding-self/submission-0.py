class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardPass = []
        backwardPass = []

        for i, num in enumerate(nums):
            if i == 0:
                forwardPass.append(num)
            else:
                forwardPass.append(num * forwardPass[len(forwardPass) - 1])
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                backwardPass.append(num)
            else:
                backwardPass.append(nums[i] * backwardPass[len(backwardPass) - 1])
        solution = []

        for i in range(len(nums)):
            if i == 0:
                solution.append(backwardPass[len(backwardPass) - 2])
            elif i == len(nums) - 1:
                solution.append(forwardPass[len(forwardPass) - 2])
            else:
                solution.append(forwardPass[i - 1] * backwardPass[len(nums) - i - 2])

        return solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        solution = []
        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                tempVal = nums[l] + nums[r]
                if num + tempVal == 0:
                    tempArr = [nums[i],nums[l],nums[r]]
                    if tempArr not in solution:
                        solution.append(tempArr)
                    l += 1
                    r -= 1
                elif 0 > num + tempVal:
                    l += 1
                else:
                    r -= 1
        return solution
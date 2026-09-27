import copy
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solutions = []

        def solutionFinder(sol, i):
            nonlocal solutions
            while i < len(nums):
                sol.append(nums[i])
                sumTotal = sum(sol)
                if sumTotal == target:
                    solutions.append(copy.deepcopy(sol))
                    sol.pop()
                elif sumTotal > target:
                    sol.pop()
                else:
                    solutionFinder(sol, i)
                i += 1
            if sol:
                sol.pop()
        solutionFinder([], 0)
        return solutions
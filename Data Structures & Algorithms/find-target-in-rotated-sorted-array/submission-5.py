class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) //2
            if nums[m] == target:
                return m
            
            if target < nums[m]:
                if nums[l] <= nums[m] and nums[l] <= target:
                    r = m - 1
                elif nums[l] > nums[m] and nums[l] > target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[r] >= nums[m] and nums[r] >= target:
                    l = m + 1
                elif nums[r] < nums[m] and nums[r] < target:
                    l = m + 1
                else:
                    r = m - 1

        return -1
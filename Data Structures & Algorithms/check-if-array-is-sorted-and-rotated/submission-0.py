class Solution:
    def check(self, nums: List[int]) -> bool:
        minVal = min(nums)

        i = 0
        while i < len(nums):
            if nums[i] == minVal:
                break
            i += 1
        
        j = 1

        while j < len(nums):
            # print(nums[i % len(nums)], nums[(i + 1) % len(nums)])
            if nums[i % len(nums)] > nums[(i + 1) % len(nums)]:
                return False
            j += 1
            i += 1
        return True
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while True:
            m = (r + l) //2
            # print(l,m,r)

            if nums[l] < nums[m] and nums[m] < nums[r]:# it is in the 1st half
                r = m
            elif nums[l] > nums[m] and nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:# it is in the 2nd half
                l = m + 1
            else:
                return nums[m]
        return 0
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) <= 3:
            try:
                if nums[0] == target:
                    return 0
                elif nums[1] == target:
                    return 1
                elif nums[2] == target:
                    return 2
            except:
                return -1

        while l <= r:
            m = (r + l) //2
            # print(l, m , r)
            if nums[m] == target:
                return m
            
            if target < nums[m]:
                if nums[l] <= nums[m] and nums[l] <= target:
                    r = m - 1
                elif nums[l] > nums[m] and nums[l] > target:
                    r = m - 1
                else:
                    l = m + 1
                # if nums[l] > nums[m]:
                #     r = m - 1
                # elif nums[l] <= nums[m] and nums[l] <= target:
                #     r = m - 1
                # elif nums[l] < nums[m]:
                #     l = m + 1
                # else:
                #     return -1
            else:
                if nums[r] >= nums[m] and nums[r] >= target:
                    l = m + 1
                elif nums[r] < nums[m] and nums[r] < target:
                    l = m + 1
                else:
                    r = m - 1
                # if nums[m] < nums[r]:
                #     l = m + 1
                # elif nums[m] < nums[r] and nums[r] >= target:
                #     l = m + 1
                # elif nums[m] > nums[r]:
                #     r = m - 1
                # else:
                #     return -1

        return -1
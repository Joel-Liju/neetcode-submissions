class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums)

        while lp < rp:
            mp = (lp + rp) // 2
            if nums[mp] == target:
                return mp
            elif nums[mp] > target:
                rp = mp
            else:
                lp = mp + 1
        
        return - 1
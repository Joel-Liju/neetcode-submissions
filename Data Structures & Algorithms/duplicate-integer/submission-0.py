class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}

        for num in nums:
            try:
                if vals[num]:
                    return True
            except:
                vals[num] = True
        return False
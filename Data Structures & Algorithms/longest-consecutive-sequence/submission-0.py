class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = {}

        for num in nums:
            vals[num] = True

        for num in nums:
            try:
                if vals[num - 1] or not vals[num - 1]:
                    vals[num] = False
            except:
                pass


        longestLength = 0
        for val in vals:
            if vals[val]:
                length = 1
                try:
                    while not vals[val + length]:
                        length += 1
                except:
                    longestLength = max(longestLength, length)

        return longestLength
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq tracker
        freqNo = [[] for _ in range(len(nums) + 1)]
        vals = {}

        for num in nums:
            try:
                vals[num] += 1
            except:
                vals[num] = 1
        for val in vals:
            freqNo[vals[val]].append(val)
        solution = []

        for i in range(len(nums), -1, - 1):
            if len(solution) == k:
                break
            solution += freqNo[i]
            # print(solution)
        return solution
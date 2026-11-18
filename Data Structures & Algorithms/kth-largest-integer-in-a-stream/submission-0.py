class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse = True)

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.nums):
            if self.nums[i] <= val:
                self.nums.insert(i,val)
                break
            i += 1
        if i == len(self.nums):
            self.nums.append(val)
        return self.nums[self.k - 1]

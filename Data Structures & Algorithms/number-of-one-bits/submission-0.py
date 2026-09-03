class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n > 0:
            b = n % 2
            if b == 1:
                counter += 1
            n = n//2
        return counter
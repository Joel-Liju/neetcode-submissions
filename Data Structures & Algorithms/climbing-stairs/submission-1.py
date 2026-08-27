class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        vals = [0] * n
        
        vals[0] = 1
        vals[1] = 2

        for i in range(2, n):
            vals[i] = vals[i - 1] + vals[i - 2]

        return vals[-1]
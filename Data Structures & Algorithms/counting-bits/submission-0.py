class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = []

        for i in range(n + 1):
            tempI = i
            val = 0
            while tempI > 0:
                if tempI & 1 == 1:
                    val += 1
                tempI = tempI >> 1
            sol.append(val)
        return sol
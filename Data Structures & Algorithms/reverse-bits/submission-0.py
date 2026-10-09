class Solution:
    def reverseBits(self, n: int) -> int:
        reversedBits = ""
        while n > 0:
            if n & 1 == 1:
                reversedBits += "1"
            else:
                reversedBits += "0"
            n = n >> 1
        while len(reversedBits) < 32:
            reversedBits += "0"
        return int(reversedBits, base=2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        numOfPOdds = [1] * len(s)

        # Odds will be counted. 
        for i in range(1, len(s)):
            l, r = i - 1, i + 1

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                numOfPOdds[i] += 1
                l -= 1
                r += 1

        # Evens need to be counted. 
        numOfPEvens = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                numOfPEvens[i] += 1
                l, r = i - 2, i + 1
                while l >= 0 and r < len(s):
                    if s[l] != s[r]:
                        break
                    numOfPEvens[i] +=1
                    l -= 1
                    r += 1
        # print(numOfPOdds, numOfPEvens)

        return sum(numOfPOdds) + sum(numOfPEvens)
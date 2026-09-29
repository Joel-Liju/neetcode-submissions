class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        breakIdxs = [0]

        for i in range(len(s) + 1):
            idx = 0
            while idx < len(breakIdxs):
                if s[breakIdxs[idx]: i] in wordDict:
                    breakIdxs.append(i)
                    break
                idx += 1
        return breakIdxs[-1] == len(s)
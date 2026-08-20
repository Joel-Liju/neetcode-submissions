class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        # now assume that length of 2 of string
        vals = {}
        maxLength = 1
        vals[s[0]] = True
        l = 0
        r = 0
        r += 1
        while r < len(s):
            try:
                if vals[s[r]]:
                    maxLength = max(maxLength, r - l)
                    while vals[s[r]]:
                        vals[s[l]] = False
                        l += 1
                    continue
                else:
                    vals[s[r]] = True
            except:
                vals[s[r]] = True
            r += 1
        return max(maxLength, r - l)
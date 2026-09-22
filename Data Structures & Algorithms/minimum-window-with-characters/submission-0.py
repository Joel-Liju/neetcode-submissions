class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for ltr in t:
            countT[ltr] = 1 + countT.get(ltr,0)
        
        have, need = 0, len(countT)

        res = [-1, -1]
        resLen = float('inf')
        
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and countT[c] == window[c]:
                have += 1

            while have >= need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l,r]
                window[s[l]] -= 1

                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        if have >= need:
            if (r - l) < resLen:
                resLen = r - l
                res = [l,r]
        return s[res[0]: res[1] + 1]
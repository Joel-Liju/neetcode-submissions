class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # have a l and r as 0
        # have a dictionary of counters of letters
        # as soon as the min of the values is > k then move till it is not.
        # keep track of max when this happens

        l, r = [0,0]
        counts = {}
        maxLength = 0

        while r < len(s):
            try:
                counts[s[r]] += 1
            except:
                counts[s[r]] = 1
            if sum(counts.values()) - max(counts.values()) > k:
                # there is an issue
                maxLength = max(maxLength, r - l)
                while l < r and sum(counts.values()) - max(counts.values()) > k:
                    counts[s[l]] -= 1
                    l += 1
            r += 1

        return max(maxLength, r - l)
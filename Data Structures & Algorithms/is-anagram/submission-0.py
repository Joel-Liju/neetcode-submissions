class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vals = {}
        
        if len(s) != len(t):
            return False
            
        for ltr in s:
            try:
                vals[ltr] += 1
            except:
                vals[ltr] = 1
        

        for ltr in t:
            try:
                vals[ltr] -= 1
                if vals[ltr] < 0:
                    return False
            except:
                return False
        return True
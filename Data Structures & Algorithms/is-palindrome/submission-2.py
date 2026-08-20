class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = 0
        s2 = len(s) - 1
        while s1 < s2:
            try:
                while not s[s1].isalnum():
                    s1 += 1
                while not s[s2].isalnum():
                    s2 -= 1
            except:
                return True
            
            if s1 >= s2:
                break
            print(s[s1], s[s2])
            if s[s1].lower() != s[s2].lower():
                return False
            s1 += 1
            s2 -= 1
        return True
import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counts = {}
        for l in s1:
            try:
                counts[l] += 1
            except:
                counts[l] = 1
        
        for i, l in enumerate(s2):
            if l in s1:
                lp = i
                rp = i + len(s1)

                if rp > len(s2):
                    return False
                
                tmp = copy.deepcopy(counts)
                flag = True
                for ltr in s2[lp:rp]:
                    try:
                        tmp[ltr] -= 1
                        if tmp[ltr] < 0:
                            flag = False
                            break
                    except:
                        flag = False
                        break
                if flag:
                    return True

        return False
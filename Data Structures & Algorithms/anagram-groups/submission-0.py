class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort it into len as I don't think letter matters. As if it is an anagram then it will be same length. 
        vals = {}
        for i,val in enumerate(strs):
            temp = "".join(sorted(val))
            # print(temp)
            try:
                vals[temp].append(i)
            except:
                vals[temp] = [i]
        solution = []

        for val in vals:
            tempSol = []
            for i in vals[val]:
                tempSol.append(strs[i])
            solution.append(tempSol)
        return solution
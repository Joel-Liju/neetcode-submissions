class Solution:

    def encode(self, strs: List[str]) -> str:
        val = ""
        if len(strs) == 0:
            return "empty"
        for i, string in enumerate(strs):
            for j, ltr in enumerate(string):
                val += str(ord(ltr))
                if j != len(string) - 1:
                    val+= "|"
            if i != len(strs) - 1:
                val += " "
        return val
    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        tempVals = s.split(" ")
        vals = []
        for val in tempVals:
            tempStrings = val.split("|")
            tempString = ""
            for ltr in tempStrings:
                if ltr == '':
                    break
                if int(ltr) == -1:
                    tempString+=''
                else:
                    tempString += chr(int(ltr))
            vals.append(tempString)
        return vals
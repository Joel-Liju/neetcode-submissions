class TriNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:
    def __init__(self):
        self.head = TriNode()

    def addWord(self, word: str) -> None:
        ptr = self.head
        for l in word:
            try:
                ptr = ptr.children[l]
            except:
                ptr.children[l] = TriNode()
                ptr = ptr.children[l]
        ptr.endOfWord = True

    def search(self, word: str) -> bool:
        ptr = self.head
        def dfsSearch(word: str, i : int, ptr: TriNode):
            if len(word) == i:
                return ptr.endOfWord
            if word[i] == '.':
                for l in ptr.children:
                    if dfsSearch(word,i+1,ptr.children[l]):
                        return True
                return False
            if word[i] not in ptr.children:
                return False
            else:
                return dfsSearch(word, i + 1, ptr.children[word[i]])
        return dfsSearch(word,0,ptr)
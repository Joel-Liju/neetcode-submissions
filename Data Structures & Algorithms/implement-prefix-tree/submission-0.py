class TriNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class PrefixTree:
    def __init__(self):
        self.head = TriNode()
    def insert(self, word: str) -> None:
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
        for l in word:
            if l not in ptr.children:
                return False
            ptr = ptr.children[l]
        return ptr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        ptr = self.head
        for l in prefix:
            if l not in ptr.children:
                return False
            ptr = ptr.children[l]
        return True

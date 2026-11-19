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
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tri = WordDictionary()
        for word in words:
            tri.addWord(word)
        def dfs(i,j,trie, oldWord, foundWords, visited):
            if i < 0 or i >= len(board):
                return
            if j < 0 or j >= len(board[0]):
                return
            if (i,j) in visited:
                return
            if board[i][j] not in trie.children:
                return 

            visited.add((i,j))
            
            newWord = oldWord + board[i][j]
            trie = trie.children[board[i][j]]
            if trie.endOfWord:
                result.add(newWord)
            dfs(i, j + 1, trie, newWord, result, visited)
            dfs(i + 1, j, trie, newWord, result, visited)
            dfs(i, j - 1, trie, newWord, result, visited)
            dfs(i - 1, j, trie, newWord, result, visited)
            
            visited.remove((i,j))
        
        result = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in tri.head.children:
                    visited = set()
                    visited.add((i,j))
                    newWord = board[i][j]
                    if newWord in words:
                        result.add(newWord)
                    
                    dfs(i, j + 1, tri.head.children[board[i][j]], newWord, result, visited)
                    dfs(i + 1, j, tri.head.children[board[i][j]], newWord, result, visited)
                    dfs(i, j - 1, tri.head.children[board[i][j]], newWord, result, visited)
                    dfs(i - 1, j, tri.head.children[board[i][j]], newWord, result, visited)
        return list(result)
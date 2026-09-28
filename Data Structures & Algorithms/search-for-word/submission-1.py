class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def isPartOfWord(i, pos, path) -> bool:
            # print(pos, word[i])
            # print(path)
            if pos[0] >= len(board) or pos[0] < 0:
                return False
            if pos[1] >= len(board[0]) or pos[1] < 0:
                return False
            if board[pos[0]][pos[1]] != word[i]:
                return False
            if i >= len(word):
                return False
            if [pos[0], pos[1]] in path:
                return False
            if i == len(word) - 1:
                return True
            path.append([pos[0], pos[1]])
            for incI, incJ in [[1,0], [0, 1], [-1, 0], [0,-1]]:
                loc = [pos[0] + incI, pos[1] + incJ]
                if isPartOfWord(i + 1, loc, path):
                    return True
            if path:
                path.pop()
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    flag = isPartOfWord(0, [i,j], [])
                    if flag:
                        return flag
        return False
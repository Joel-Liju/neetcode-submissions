class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = { i : [] for i in range(9)}
        cols = { i : [] for i in range(9)}
        boxes = { i : [] for i in range(9)}
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num == '.':
                    continue
                if num in rows[i]:
                    return False
                else:
                    rows[i].append(num)
                if num in cols[j]:
                    return False
                else:
                    cols[j].append(num)
                
                pos = ((i // 3) * 3) + (j // 3)

                if num in boxes[pos]:
                    return False
                else:
                    boxes[pos].append(num)
            # print(rows)
            # print(cols)
            # print(boxes)
            # print()
        return True
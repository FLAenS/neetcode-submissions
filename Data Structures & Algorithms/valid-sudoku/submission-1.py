class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == '.':
                    continue
                box = (i // 3, j // 3)
                if x in cols[j] or x in rows[i] or x in boxes[box]:
                    return False
                rows[i].add(x)
                cols[j].add(x)
                boxes[box].add(x)
        return True
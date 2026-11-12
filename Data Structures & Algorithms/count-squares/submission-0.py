class CountSquares:

    def __init__(self):
        self.x2y = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x2y[x][y] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0
        for y, cnt in self.x2y[qx].items():
            if y == qy:
                continue
            d = y - qy
            for x in (qx + d, qx - d):
                res += cnt * self.x2y[x][qy] * self.x2y[x][y]
        return res

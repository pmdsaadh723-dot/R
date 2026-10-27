class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        row0 = '.'*(n)
        grid.append(row0)
        for i in range(1, m):
            row = '#'*(n-1) + '.'
            grid.append(row)
        return grid
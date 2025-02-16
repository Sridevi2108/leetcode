from typing import List

class Solution:
    def mark0(self, grid: List[List[str]], i: int, j: int, n: int, m: int):
        if (i < 0 or j < 0):
            return
        if (i >= n or j >= m):
            return
        if (grid[i][j] == '0'):
            return
        grid[i][j] = '0'
        self.mark0(grid, i - 1, j, n, m)
        self.mark0(grid, i + 1, j, n, m)
        self.mark0(grid, i, j - 1, n, m)
        self.mark0(grid, i, j + 1, n, m)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):

                if (grid[i][j] == '1'):
                    count += 1
                    self.mark0(grid, i, j, n, m)
        return count

if __name__=="__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    solution=Solution()
    result=solution.numIslands(grid)
    print(result)


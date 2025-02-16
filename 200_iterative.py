from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n=len(grid)
        m=len(grid[0])
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    count+=1
                    stack=[(i,j)]
                    while stack:
                        x,y=stack.pop()
                        if 0<=x<n and 0<=y<m and grid[x][y]=='1':
                            grid[x][y]='0'
                            stack.append((x-1,y))
                            stack.append((x+1,y))
                            stack.append((x,y-1))
                            stack.append((x,y+1))
        return count
if __name__=="__main__":
    grid = [
        ["1", "1", "1","0"],
        ["1", "1", "0", "0"],
        ["0", "0", "0", "1"]
    ]
    solution=Solution()
    result=solution.numIslands(grid)
    print(result)


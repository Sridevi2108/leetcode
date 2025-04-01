import math


class Solution:
    def numTrees(self, n: int) -> int:
        return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))

if __name__=="__main__":
    n=3
    solution=Solution()
    result=solution.numTrees(n)
    print(result)
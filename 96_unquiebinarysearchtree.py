import math


class Solution:
    def factorial(self,num):
        result=1
        for i in range(2,num+1):
            result*=i
        return result
    def numTrees(self, n: int) -> int:
        return self.factorial(2 * n) // (self.factorial(n + 1) * self.factorial(n))

if __name__=="__main__":
    n=3
    solution=Solution()
    result=solution.numTrees(n)
    print(result)
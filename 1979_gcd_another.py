import math
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        while b != 0:
            r = a % b
            a = b
            b = r
        return a
if __name__=="__main__":
    nums=[2,5,6,9,10]
    solution=Solution()
    result=solution.findGCD(nums)
    print(result)



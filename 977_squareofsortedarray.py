from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        var = []
        for i in range(len(nums)):
            square = nums[i] ** 2
            var.append(square)
        var.sort()
        return var

if __name__=="__main__":
    nums = [-4, -1, 0, 3, 10]
    solution=Solution()
    result=solution.sortedSquares(nums)
    print(result)


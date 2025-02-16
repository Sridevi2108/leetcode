from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_list=[num**2 for num in nums]
        sq_list.sort()
        return sq_list

if __name__=="__main__":
    nums = [-4, -1, 0, 3, 10]
    solution=Solution()
    result=solution.sortedSquares(nums)
    print(result)


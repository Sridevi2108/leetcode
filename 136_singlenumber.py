from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for i in nums:
            if nums.count(i) == 1:
                return i
if __name__=="__main__":
    nums = [2, 2, 1]
    solution=Solution()
    result=solution.singleNumber(nums)
    print(result)
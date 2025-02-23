from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        min_sum=0
        min_length=float('inf')
        for right in range(len(nums)):
            min_sum+=nums[right]
            while min_sum>=target:
                min_length=min(min_length,right-left+1)
                min_sum-=nums[left]
                left+=1
        return min_length if min_length!=float('inf') else 0

if __name__=="__main__":
    nums = [2,3,1,2,4,3]
    target=7
    solution=Solution()
    result=solution.minSubArrayLen(target,nums)
    print(result)
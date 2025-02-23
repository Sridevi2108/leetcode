from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mincount = float('inf')

        for i in range(len(nums)):
            sum = nums[i]
            count = 1
            if sum>=target:
                return 1
            for j in range(i+1, len(nums)):
                sum += nums[j]
                count += 1
                if sum >= target:
                    mincount = min(mincount,count)
                    break
        return mincount if mincount!=float('inf') else 0


if __name__=="__main__":
    nums = [1,1,1,1,1,1,1,1]
    target=11
    solution=Solution()
    result=solution.minSubArrayLen(target,nums)
    print(result)
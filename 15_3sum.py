from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif s > 0:
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif s < 0:
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result

if __name__=="__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    solution=Solution()
    result=solution.threeSum(nums)
    print(result)






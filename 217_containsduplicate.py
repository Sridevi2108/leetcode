from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left,right=0,1
        while right<len(nums):
            if nums[left]==nums[right]:
                return True
            left+=1
            right+=1
        return False


if __name__ == "__main__":
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # Example input
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)

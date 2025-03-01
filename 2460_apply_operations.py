from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1
        for i in range(len(nums) - 1):
            if nums[left] == nums[right]:
                nums[left] = nums[left] * 2
                nums[right] = 0
            left += 1
            right += 1
        lst = []
        for i in range(len(nums)):
            if nums[i] != 0:
                lst.append(nums[i])
        lst.extend([0] * (len(nums) - len(lst)))

        return lst

if __name__=="__main__":
    nums=[1,2,2,1,1,0]
    solution=Solution()
    result=solution.applyOperations(nums)
    print(result)
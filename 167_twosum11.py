from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
if __name__=="__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    solution=Solution()
    result=solution.twoSum(numbers,target)
    print(result)



from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        result = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)
            if (height[left] < height[right]):
                left = left + 1
            else:
                right -= 1
        return result
if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # Example input
    solution = Solution()
    max_water = solution.maxArea(height)
    print("Maximum water that can be stored:", max_water)

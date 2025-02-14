class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        nums.sort()
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual
if __name__ == "__main__":
    nums = [0, 1]  # Example input
    solution = Solution()
    result = solution.missingNumber(nums)
    print(result)
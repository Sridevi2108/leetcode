class Solution:
    def findDisappearedNumbers(self, nums):
        n = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in n:
                result.append(i)
        return result
if __name__=="__main__":
    nums=[1,1]
    solution=Solution()
    result=solution.findDisappearedNumbers(nums)
    print(result)

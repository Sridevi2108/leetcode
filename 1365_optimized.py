class Solution:
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        d = {}
        for i, num in enumerate(temp):
            if num not in d:
                d[num] = i
        result = []
        for i in nums:
            result.append(d[i])
        return result

if __name__=="__main__":
    nums = [8,1,2,2,3]
    solution=Solution()
    result=solution.smallerNumbersThanCurrent(nums)
    print(result)

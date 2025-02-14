class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            result.append(count)
        return result
if __name__=="__main__":
    nums = [8, 1, 2, 2, 3]
    solution=Solution()
    result=solution.smallerNumbersThanCurrent(nums)
    print(result)

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in hashmap:
                return (hashmap[val], i)
            hashmap[num] = i
        return []

if __name__=="__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution=Solution()
    result=solution.twoSum(nums,target)
    print(result)
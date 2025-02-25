from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap=set()
        for num in nums:
            if num in hashmap:
                hashmap.remove(num)
            else:
                hashmap.add(num)
        return hashmap.pop()
    # def singleNumber(self, nums: List[int]) -> int:
    #     xor=0
    #     for i in nums:
    #         xor^=i
    #     return xor

if __name__=='__main__':
    nums=[2,2,1]
    solution=Solution()
    result=solution.singleNumber(nums)
    print(result)

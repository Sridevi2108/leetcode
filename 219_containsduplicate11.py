from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}
        for i,num in enumerate(nums):
            if num in hashmap and abs(hashmap[num]-i)<=k:
                return True
            hashmap[num]=i
        return False

if __name__=="__main__":
    nums = [1, 2, 3]
    k = 3
    solution=Solution()
    result=solution.containsNearbyDuplicate(nums,k)
    print(result)
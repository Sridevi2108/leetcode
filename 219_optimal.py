from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = set()
        for i, num in enumerate(nums):
            if num in hashmap:
                return True
            hashmap.add(num)
            if len(hashmap) > k:
                hashmap.remove(nums[i - k])
        return False
if __name__=="__main__":
    nums = [1, 2, 3, 1]
    k=3
    solution=Solution()
    result=solution.containsNearbyDuplicate(nums,k)
    print(result)


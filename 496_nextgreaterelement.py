from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        for num in nums1:
            next_greater=-1
            found=False
            for j in range(len(nums2)):
                if nums2[j]==num:
                    found=True
                if found and nums2[j]>num:
                    next_greater=nums2[j]
                    break
            lst.append(next_greater)
        return lst
if __name__=="__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    solution=Solution()
    result=solution.nextGreaterElement(nums1,nums2)
    print(result)


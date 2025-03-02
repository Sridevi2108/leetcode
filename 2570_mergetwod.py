from typing import List
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        merge = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                merge.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1
        while i < len(nums1):
            merge.append(nums1[i])
            i += 1
        while j < len(nums2):
            merge.append(nums2[j])
            j += 1
        return merge

if __name__=="__main__":
    nums1 =[[1, 2], [2, 3], [4, 5]]
    nums2 =[[1, 4], [3, 2], [4, 1]]
    solution=Solution()
    result=solution.mergeArrays(nums1,nums2)
    print(result)
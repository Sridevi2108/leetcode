from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minval=float('inf')
        for i in range(len(arr)-1):
            minval=min(minval,arr[i+1]-arr[i])
        result=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==minval:
                result.append([arr[i],arr[i+1]])
        return result
if __name__=="__main__":
    arr = [4, 2, 1, 3]
    solution=Solution()
    result=solution.minimumAbsDifference(arr)
    print(result)
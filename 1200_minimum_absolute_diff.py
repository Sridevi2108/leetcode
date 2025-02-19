from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        i = 0
        #if (arr[i] >=0 and arr[i + 1] >= 0) or (arr[i] <=0 and arr[i + 1] <= 0):
        #   minval = arr[i + 1] - arr[i]
        #else:
        minval = max(arr)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] - arr[i] < minval:
                    minval = min(minval, (arr[j] - arr[i]))

        result = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] - arr[i] == minval:
                    result.append([arr[i], arr[j]])
        return result

if __name__=="__main__":
    arr =[-25,-51,-29,-23,57,-18]
    solution=Solution()
    result=solution.minimumAbsDifference(arr)
    print(result)
import math
class Solution:
    def greatestcommondivisor(self,nums):
        return math.gcd(min(nums),max(nums))

if __name__=="__main__":
    nums=[2,5,6,9,10]
    solution=Solution()
    result=solution.greatestcommondivisor(nums)
    print(result)
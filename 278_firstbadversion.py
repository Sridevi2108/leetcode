def isBadVersion(version):
    bad = 4
    return version >= bad
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=1
        right=n
        while left<right:
            mid=(left+right)//2
            if isBadVersion(mid):
                right=mid
            else:
                left=mid+1
        return left

if __name__=="__main__":
    solution=Solution()
    n=5
    print("First Bad version:",solution.firstBadVersion(n))


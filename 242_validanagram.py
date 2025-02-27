class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        else:
            return False

if __name__=="__main__":
    s = "anagram"
    t="nagaram"
    solution=Solution()
    result=solution.isAnagram(s,t)
    print(result)
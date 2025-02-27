from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return 0
        char_count=Counter(s)
        for char in t:
            char_count[char]-=1
            if char_count[char]<0:
                return False
        return True
if __name__=="__main__":
    s = "anagram"
    t="nagaram"
    solution=Solution()
    result=solution.isAnagram(s,t)
    print(result)
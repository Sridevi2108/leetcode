class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for i in ransomNote:
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True

if __name__=="__main__":
    ransomNote = "a"
    magazine = "b"
    solution=Solution()
    result=solution.canConstruct(ransomNote,magazine)
    print(result)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        string=s+s
        if goal in string and len(s)==len(goal):
            return True
        else:
            return False

if __name__=="__main__":
    s = "abcde"
    goal = "cdeab"
    solution=Solution()
    result=solution.rotateString(s,goal)
    print(result)
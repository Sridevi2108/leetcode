class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"(":")","{":"}","[":"]"}
        for i in s:
            if i in d.keys():
                stack.append(i)
            else:
                if stack==[]:
                    return False
                else:
                    if d[stack[-1]]==i:
                        stack.pop()
                    else:
                        return False
        if stack==[]:
            return True
        else:
            return False

if __name__=="__main__":
    s = "()"
    solution=Solution()
    result=solution.isValid(s)
    print(result)
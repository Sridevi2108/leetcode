class Solution:
    def harshandnumber(self,x):
        temp=x
        sumofdigit=0
        while(x>0):
            var=x%10
            sumofdigit+=var
            x = x // 10
        if (temp % sumofdigit == 0):
            return sumofdigit
        return -1

if __name__=="__main__":
    x=18
    solution=Solution()
    result=solution.harshandnumber(x)
    print(result)
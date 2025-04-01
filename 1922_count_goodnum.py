class Solution:
    Mod = 1000000007
    def power(self,x,y):
        res=1
        while(y>0):
            if y%2==1:
                res=(res*x)%self.Mod
            x=x*x%self.Mod
            y=y//2
        return res

    def countGoodNumbers(self, n: int) -> int:
        even_positions=(n+1)//2
        odd_positions=n//2
        result=(self.power(5,even_positions)*self.power(4,odd_positions))%self.Mod
        return result

if __name__=="__main__":
    n=4
    solution=Solution()

    result=solution.countGoodNumbers(n)
    print(result)

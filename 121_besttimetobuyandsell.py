from typing import List
class Solution:
    def maxprofit(self,prices:List[int])->int:
        left,right=0,1
        maxprice=0
        while right!=len(prices):
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                maxprice=max(profit,maxprice)
            else:
                left=right
            right+=1
        return maxprice
if __name__=="__main__":
    prices = [1,2,4,2,5,7,2,4,9,0,9]
    solution=Solution()
    result=solution.maxprofit(prices)
    print(result)


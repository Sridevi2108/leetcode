class Solution:
    def delayedtime(self,arrivaltime,delayedtime):
        totaltime=(arrivaltime+delayedtime)%24
        return totaltime


if __name__=="__main__":
    arrivaltime=1
    delayedtime=24
    solution=Solution()
    result=solution.delayedtime(arrivaltime,delayedtime)
    print(result)
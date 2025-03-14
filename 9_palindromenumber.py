def ispalindrome(x:int)->bool:
    temp=x
    pal=0
    while(x>0):
        val=x%10
        pal=pal*10+val
        x=x//10
    if pal==temp:
        return True
    return False
#return str(x)==str(x)[::-1]
if __name__=="__main__":
    x=121
    result=ispalindrome(x)
    print(result)
N=int(input())
s=input()
x,y=map(int,input().split())

def case(a,b,s):
    if a==x:
        r1=s[x].swapcase()
        print(r1,end="")
        print(s[1:y],end="")
    if b==y:
        r2=s[y].swapcase()
        print(r2,end="")
        print(s[y+1:])
    
        
        
        
case(x,y,s)
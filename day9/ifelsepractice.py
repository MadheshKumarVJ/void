#GIANT WHEEL-Codechef
x=int(input())
if x>=60:
    print("yes")
else:
    print("no")


#Water mixing - codechef
for t in range(int(input())):
    a,b,x,y=map(int,input().split())
    if b>=a:
        if x+a>=b:
            print("yes")
        else:
            print("no")
    else:
        if a-y<=b:
            print("yes")
        else:
            print("no")
        

#Trade surplus - codechef
for t in range(int(input())):
    a,b,c,d=map(int,input().split())
    x=a-b
    y=c-d
    if x+y<0:
        print("yes")
    else:
        print("no")

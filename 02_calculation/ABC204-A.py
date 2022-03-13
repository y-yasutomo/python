x,y = map(int,input().split())
print((x+y)//2 if (x+y)%2==0 else (3-(x+y)%3)%3)
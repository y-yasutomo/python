a,b,c,x = map(int,input().split())
print(1 if x<=a else c  /(b-a) if x>a and x<=b else 0)
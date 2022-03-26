a,b,c = map(int,input().split())
print(a if b==c else b if c==a else c if a==b else 0)
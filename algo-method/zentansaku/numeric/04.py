a,b = map(int,input().split())
n = min(a,b)
ans = 1
for i in range(1,n+1) :
    if a%i==0  and b%i==0 :
        ans = i

print(ans)

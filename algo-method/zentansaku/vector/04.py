n,v = map(int,input().split())
x = list(map(int, input().split()))
ans = -1
for i in range(n) :
    if x[i] == v :
       ans = i

print(ans)
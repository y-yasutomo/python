n = int(input())
a = list(map(int, input().split()))
ans = [0]*9
for i in a :
    ans[i-1]+=1

print(ans.index(max(ans))+1)
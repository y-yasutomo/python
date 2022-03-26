n = int(input())
a = list(map(int, input().split()))
ans = 0
Max = a[0]
for i in range(1,n) :
    if a[i] > Max :
        Max = a[i]
        ans = i

print(ans)
n,v = map(int(),input().split())
x = list(map(int, input().split()))
for i in x :
    if v in i :
        print("Yes")
        break
else :
    print("No")
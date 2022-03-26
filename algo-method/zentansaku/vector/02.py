n,v = map(int,input().split())
x = list(map(int, input().split()))
for i in x :
    if i == v :
        print("Yes")
        break
else :
    print("No")

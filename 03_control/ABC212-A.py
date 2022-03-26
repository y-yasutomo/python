a,b = map(int,input().split())
print("Alloy" if a>0 and b>0 else "Gold" if a>0 and b==0 else "Silver")
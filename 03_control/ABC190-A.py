a,b,c = map(int,input().split())
if c == 0 :
    print("Aoki" if a<=b else "Takahashi")
else : 
    print("Takahashi" if b<=a else "Aoki")

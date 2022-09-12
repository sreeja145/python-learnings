inp = list(map(float,input().split()))
a=int(1)
for i in inp:
    i=float(i)
    a=a*i;
a=float(a/100)
print(round(a,2))

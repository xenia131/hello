a, b, c = map(int, input().split(","))
if a == min(a,b,c):
    if b == min(b,c):
        print(a,b,c)
    else:
        print(a,c,b)
elif b == min(a,b,c):
    if a == min(a,c):
        print(b,a,c)
    else:
        print(b,c,a)
elif b == min(a,b):
    print(c,b,a)
else:
    print(c,a,b)
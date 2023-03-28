a = 3
b = 7
c = 9

if a < b and c > a:
    if a + b > c:
        print("Path A")
    elif b + c < a:
        print("Path B")
elif a < b:
    print("Path C")
else:
    print("Path D")
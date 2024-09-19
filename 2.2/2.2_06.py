n = int(input())
if n % 100 == 0 and n > 0:
    if n % 400 == 0:
        print("YES")
    else:
        print("NO")
elif n % 4 == 0 and n > 0:
    print("YES")
else:
    print("NO")
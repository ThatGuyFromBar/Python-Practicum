n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
sum = n * m
tr = n
while tr * k1 + (n - tr) * k2 != sum:
    tr -= 1
print(f"{tr} {n - tr}")
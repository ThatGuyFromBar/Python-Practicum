n = int(input())
m = int(input())
t = int(input())
mins = (n * 60 + m + t) % 1440
n = str(mins // 60)
if len(n) < 2:
    n = "0" + n
m = str(mins % 60)
if len(m) < 2:
    m = "0" + m
print(f"{n}:{m}")
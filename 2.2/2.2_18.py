a = float(input())
b = float(input())
c = float(input())
s = [a, b, c]
m1 = min(s)
s.remove(m1)
m2 = min(s)
m3 = max(s)
if m3 ** 2 < m2 ** 2 + m1 ** 2:
    print("крайне мала")
elif m3 ** 2 > m2 ** 2 + m1 ** 2:
    print("велика")
else:
    print("100%")
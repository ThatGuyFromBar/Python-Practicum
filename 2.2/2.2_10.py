n = int(input())
s1 = int(str(n)[1]) + int(str(n)[2])
s2 = int(str(n)[0]) + int(str(n)[1])
if s1 > s2:
    print(f"{s1}{s2}")
else:
    print(f"{s2}{s1}")
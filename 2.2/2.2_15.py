n1 = input()
n2 = input()
n1 = list(n1)
s = list(n2) + n1
for i in range(len(s)):
    s[i] = int(s[i])
n1 = min(s)
n2 = max(s)
s.remove(n1)
s.remove(n2)
n3 = sum(s) % 10
print(f"{n2}{n3}{n1}")
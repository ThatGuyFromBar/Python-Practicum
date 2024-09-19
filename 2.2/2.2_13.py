s1 = input()
s2 = input()
s3 = input()
for i in range(len(s1)):
    tr = s1[i]
    if tr == s2[i] and tr == s3[i]:
        break
print(tr)